# Copyright 2023 Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import werkzeug.urls

from odoo import fields,_

from odoo import http
from odoo.http import request
from odoo.addons.website_membership.controllers.main import WebsiteMembership

class WebsiteMembershipCategory(WebsiteMembership):

    @http.route([
        '/members',
        '/members/page/<int:page>',

        '/members/country/<int:country_id>',
        '/members/country/<country_name>-<int:country_id>',
        '/members/country/<int:country_id>/page/<int:page>',
        '/members/country/<country_name>-<int:country_id>/page/<int:page>',

        '/members/category/<int:category_id>',
        '/members/category/<int:category_id>/page/<int:page>',

        '/members/country/<int:country_id>/category/<int:category_id>',
        '/members/country/<int:country_id>/category/<int:category_id>/page/<int:page>',
        '/members/country/<country_name>-<int:country_id>/category/<int:category_id>',
        '/members/country/<country_name>-<int:country_id>/category/<int:category_id>/page/<int:page>',
    ], type='http', auth="public", website=True)
    def members(self, country_id=0, category_id=0, page=1, **post):
        Country = request.env['res.country']
        Category = request.env['togezer.company_category']
        Partner = request.env['res.partner']

        post_name = post.get('search') or post.get('name', '')
        current_country = None
        current_category = None
        # base domain for groupby / searches
        search_domain = [
            ('is_company', '=', True),
            ('membership_state', 'in', ['paid', 'free']),
            ('website_published', '=', True),
            ('active', '=', True)
        ]

        if post_name:
            search_domain += ['|', ('name', 'ilike', post_name), ('website_description', 'ilike', post_name)]

        search_members = Partner.sudo().search(search_domain)
        count_members = len(search_members)

        page_domain = search_domain
        if country_id:
            page_domain += [('country_id', '=', country_id)]
        if category_id:
            page_domain += [('company_category', 'in', category_id)]

        page_members = Partner.sudo().search(page_domain)
        

        # Get Countries information
        countries = Partner.sudo().read_group(search_domain, ["id", "country_id"], groupby="country_id", orderby="country_id")
        countries_total = sum(country_dict['country_id_count'] for country_dict in countries)

        if country_id:
            current_country = Country.browse(country_id).read(['id', 'name'])[0]
            if not any(x['country_id'][0] == country_id for x in countries if x['country_id']):
                countries.append({
                    'country_id_count': 0,
                    'country_id': (country_id, current_country["name"])
                })
                countries = [d for d in countries if d['country_id']]
                countries.sort(key=lambda d: d['country_id'][1])
        

        countries.insert(0, {
            'country_id_count': countries_total,
            'country_id': (0, _("All Countries"))
        })


        base_url = '/members%s%s' % ('/country/%s' % country_id if country_id else '',
                                     '/category/%s' % category_id if category_id else '')

        # Get Categories information
        categories = Category.sudo().search([]).sorted()
        category_dict = []
        category_all = {
            "category_id_count": len(search_members),
            "id": 0,
            "name": _("All Categories"),
        }
        category_dict.append(category_all)
        for category in categories:
            category_id_count = 0
            for partner in search_members:
                if category in partner.company_category:
                    category_id_count += 1
            if category_id_count > 0:
                category_dict.append({
                    "category_id_count": category_id_count,
                    "id": category.id,
                    "name": category.name,
                })
        if category_id:
            current_cat = Category.browse(category_id)[0]
            current_category = {
                "category_id_count": 0,
                "id": current_cat.id,
                "name": current_cat.name,
            }
        else:
            current_category = category_all
        # request pager for lines
        pager = request.website.pager(url=base_url, total=count_members, page=page, step=self._references_per_page, scope=7, url_args=post)
        values = {
            'partners': page_members,
            'countries': countries,
            'current_country': current_country and [current_country['id'], current_country['name']] or None,
            'current_country_id': current_country and current_country['id'] or 0,
            'categories': category_dict,
            'current_category': current_category,
            'current_category_id': current_category['id'],
            'pager': pager,
            'post': post,
            'search': "?%s" % werkzeug.url_encode(post),
            'search_count': count_members,
        }
        return request.render("website_membership.index", values)