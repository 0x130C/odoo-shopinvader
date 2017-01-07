# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class LocomotivecmsBackend(models.Model):
    _inherit = 'locomotivecms.backend'

    pricelist_ids = fields.One2many(
        'locomotivecms.pricelist',
        'backend_id',
        'Pricelist')
