# Copyright (C) 2020 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    fsm_filter_location_by_contact = fields.Boolean(
        string="Filter Contacts with Location"
    )

    @api.onchange("fsm_filter_location_by_contact")
    def onchange_fsm_filter_location_by_contact(self):
        for fso_id in self.env["fsm.order"].search([]):
            fso_id._onchange_location_id_customer_account()
