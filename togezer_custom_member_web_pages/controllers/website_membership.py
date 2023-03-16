# Copyright 2023 Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import werkzeug.urls

from odoo import fields,_

from odoo import http
from odoo.http import request
from odoo.addons.website_membership.controllers.main import WebsiteMembership

class WebsiteMembershipCategory(WebsiteMembership):

    # @http.route([
    #     '/members',
    #     '/members/page/<int:page>',

    #     '/members/country/<int:country_id>',
    #     '/members/country/<country_name>-<int:country_id>',
    #     '/members/country/<int:country_id>/page/<int:page>',
    #     '/members/country/<country_name>-<int:country_id>/page/<int:page>',

    #     '/members/category/<int:category_id>',
    #     '/members/category/<int:category_id>/page/<int:page>',

    #     '/members/country/<int:country_id>/category/<int:category_id>',
    #     '/members/country/<int:country_id>/category/<int:category_id>/page/<int:page>',
    #     '/members/country/<country_name>-<int:country_id>/category/<int:category_id>',
    #     '/members/country/<country_name>-<int:country_id>/category/<int:category_id>/page/<int:page>',
    # ], type='http', auth="public", website=True)
    # def members(self, membership_id=None, country_name=None, country_id=0, category_id=0, page=1, **post):
    #     Product = request.env['product.product']
    #     Country = request.env['res.country']
    #     Category = request.env['togezer.company_category']
    #     MembershipLine = request.env['membership.membership_line']
    #     Partner = request.env['res.partner']

    #     post_name = post.get('search') or post.get('name', '')
    #     current_country = None
    #     current_category = None
    #     today = fields.Date.today()
    #     # base domain for groupby / searches
    #     base_line_domain = [
    #         ("partner.website_published", "=", True), ('state', '=', 'paid'),
    #         ('date_to', '>=', today), ('date_from', '<=', today)
    #     ]
    #     if membership_id and membership_id != 'free':
    #         membership_id = int(membership_id)
    #         base_line_domain.append(('membership_id', '=', membership_id))

    #     if post_name:
    #         base_line_domain += ['|', ('partner.name', 'ilike', post_name), ('partner.website_description', 'ilike', post_name)]

    #     # group by country, based on all customers (base domain)
    #     if membership_id != 'free':
    #         membership_lines = MembershipLine.sudo().search(base_line_domain)
    #         domain = [('member_lines', 'in', membership_lines.ids)]
    #         if not membership_id:
    #             domain = ['|', domain[0], ('membership_state', '=', 'free')]
    #     else:
    #         domain = [('membership_state', '=', 'free')]
    #     if post_name:
    #         domain += ['|', ('name', 'ilike', post_name), ('website_description', 'ilike', post_name)]

    #     countries = Partner.sudo().read_group(domain + [("website_published", "=", True)], ["id", "country_id"], groupby="country_id", orderby="country_id")
    #     countries_total = sum(country_dict['country_id_count'] for country_dict in countries)

    #     line_domain = list(base_line_domain)
    #     if country_id:
    #         line_domain.append(('partner.country_id', '=', country_id))
    #         current_country = Country.browse(country_id).read(['id', 'name'])[0]
    #         if not any(x['country_id'][0] == country_id for x in countries if x['country_id']):
    #             countries.append({
    #                 'country_id_count': 0,
    #                 'country_id': (country_id, current_country["name"])
    #             })
    #             countries = [d for d in countries if d['country_id']]
    #             countries.sort(key=lambda d: d['country_id'][1])
    #     if category_id:
    #         line_domain.append(('partner.company_category', 'in', category_id))

    #     countries.insert(0, {
    #         'country_id_count': countries_total,
    #         'country_id': (0, _("All Countries"))
    #     })

    #     # format domain for group_by and memberships
    #     memberships = Product.search([('membership', '=', True)], order="website_sequence")

    #     # make sure we don't access to lines with unpublished membershipts
    #     line_domain.append(('membership_id', 'in', memberships.ids))

    #     limit = self._references_per_page
    #     offset = limit * (page - 1)

    #     count_members = 0
    #     membership_lines = MembershipLine.sudo()
    #     # displayed non-free membership lines
    #     if membership_id != 'free':
    #         count_members = MembershipLine.sudo().search_count(line_domain)
    #         if offset <= count_members:
    #             membership_lines = MembershipLine.sudo().search(line_domain, offset, limit)
    #     page_partner_ids = set(m.partner.id for m in membership_lines)

    #     # get google maps localization of partners
    #     google_map_partner_ids = []
    #     if request.website.viewref('website_membership.opt_index_google_map').active:
    #         google_map_partner_ids = MembershipLine.search(line_domain).get_published_companies(limit=2000)

    #     search_domain = [('membership_state', '=', 'free'), ('website_published', '=', True)]
    #     if post_name:
    #         search_domain += ['|', ('name', 'ilike', post_name), ('website_description', 'ilike', post_name)]
    #     if country_id:
    #         search_domain += [('country_id', '=', country_id)]
    #     if category_id:
    #         search_domain += [('company_category', 'in', category_id)]
    #     free_partners = Partner.sudo().search(search_domain)

    #     memberships_data = []
    #     for membership_record in memberships:
    #         memberships_data.append({'id': membership_record.id, 'name': membership_record.name})

    #     memberships_partner_ids = {}
    #     for line in membership_lines:
    #         memberships_partner_ids.setdefault(line.membership_id.id, []).append(line.partner.id)

    #     if free_partners:
    #         memberships_data.append({'id': 'free', 'name': _('Free Members')})
    #         if not membership_id or membership_id == 'free':
    #             if count_members < offset + limit:
    #                 free_start = max(offset - count_members, 0)
    #                 free_end = max(offset + limit - count_members, 0)
    #                 memberships_partner_ids['free'] = free_partners.ids[free_start:free_end]
    #                 page_partner_ids |= set(memberships_partner_ids['free'])
    #             google_map_partner_ids += free_partners.ids[:2000-len(google_map_partner_ids)]
    #             count_members += len(free_partners)

    #     google_map_partner_ids = ",".join(str(it) for it in google_map_partner_ids)
    #     google_maps_api_key = request.website.google_maps_api_key

    #     partners = {p.id: p for p in Partner.sudo().browse(list(page_partner_ids))}

    #     base_url = '/members%s%s' % ('/country/%s' % country_id if country_id else '',
    #                                  '/category/%s' % category_id if category_id else '')

    #     # Get Categories information
    #     members = Partner.sudo().search([('membership_state', 'in', ['paid', 'free']), ('website_published', '=', True), ('active', '=', True)])
    #     categories = Category.sudo().search([]).sorted()
    #     category_dict = [{
    #         "category_id_count": len(members),
    #         "id": None,
    #         "name": _("All Categories"),
    #     }]
    #     for category in categories:
    #         category_id_count = 0
    #         for partner in members:
    #             if category in partner.company_category:
    #                 category_id_count += 1
    #         category_dict.append({
    #             "category_id_count": category_id_count,
    #             "id": category.id,
    #             "name": category.name,
    #         })
    #     if category_id:
    #         current_category = Category.browse(category_id).read(['id', 'name'])[0]
    #     # request pager for lines
    #     pager = request.website.pager(url=base_url, total=count_members, page=page, step=limit, scope=7, url_args=post)
    #     values = {
    #         'partners': partners,
    #         'memberships_data': memberships_data,
    #         'memberships_partner_ids': memberships_partner_ids,
    #         'membership_id': membership_id,
    #         'countries': countries,
    #         'current_country': current_country and [current_country['id'], current_country['name']] or None,
    #         'current_country_id': current_country and current_country['id'] or 0,
    #         'categories': category_dict,
    #         'current_category': current_category,
    #         'current_category_id': current_category and current_category['id'] or 0,
    #         'google_map_partner_ids': google_map_partner_ids,
    #         'pager': pager,
    #         'post': post,
    #         'search': "?%s" % werkzeug.url_encode(post),
    #         'search_count': count_members,
    #         'google_maps_api_key': google_maps_api_key,
    #     }
    #     return request.render("website_membership.index", values)

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