from odoo import models, fields, api

class SolarPVModuleLine(models.Model):
    _name = 'solar.pv.module.line'
    _description = 'Solar PV Module Line'

    parent_id = fields.Many2one('solar.pv.module', string="Parent Module")

    capacity = fields.Float(string="Capacity")
    panel_nos = fields.Integer(string="Panel NOS")
    amount_with_gst = fields.Float(string="Amount With GST")
    subsidy = fields.Float(string="Subsidy")
    after_subsidy_amount = fields.Float(string="After Subsidy Amount")

    @api.onchange('amount_with_gst', 'subsidy')
    def _compute_after_subsidy_amount(self):
        for rec in self:
            rec.after_subsidy_amount = rec.amount_with_gst - rec.subsidy

class SolarPVModule(models.Model):
    _name = 'solar.pv.module'
    _description = 'Solar PV Module'

    name = fields.Char(string="Module Name")

    line_ids = fields.One2many(
        'solar.pv.module.line',
        'parent_id',
        string="Module Lines"
    )
