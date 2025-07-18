from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    project_id = fields.Many2one('project.project', string="Project")
    pv_capacity_kw = fields.Float(string="PV Capacity (kW)")

    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        if self.stage_id and self.stage_id.is_won and self.project_id and self.partner_id:
            lead = self.env['project.task'].create({
                'name': self.name,
                'project_id': self.project_id.id,
                'partner_id': self.partner_id.id,
                'crm_lead_match_id': self._origin.id,
                'pv_capacity_kw': self.pv_capacity_kw
            })

    def action_set_won_rainbowman(self):
        self.ensure_one()
        self.action_set_won()

        if self.stage_id and self.stage_id.is_won and self.project_id and self.partner_id:
            lead = self.env['project.task'].create({
                'name': self.name,
                'project_id': self.project_id.id,
                'partner_id': self.partner_id.id,
                'crm_lead_match_id': self.id,
                'pv_capacity_kw': self.pv_capacity_kw
            })

        message = self._get_rainbowman_message()
        if message:
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': message,
                    'img_url': '/web/image/%s/%s/image_1024' % (self.team_id.user_id._name, self.team_id.user_id.id) if self.team_id.user_id.image_1024 else '/web/static/img/smile.svg',
                    'type': 'rainbow_man',
                }
            }
        return True