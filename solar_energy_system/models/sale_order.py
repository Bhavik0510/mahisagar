from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_id = fields.Many2one('project.project', string='Related Project', readonly=True)

    def action_create_project_custom(self):
        stage_names = [
            "Registration", "Application", "Feasibility", "Vendor Selection",
            "Upload Agreement", "Installation", "Inspection",
            "Project Commissioning", "Subsidy Request", "Subsidy Disbursal"
        ]
        stage_model = self.env['project.project.stage']
        existing_stages = stage_model.search([]).mapped('name')
        for sequence, name in enumerate(stage_names, start=1):
            if name not in existing_stages:
                stage_model.create({
                    'name': name,
                    'sequence': sequence,
                })
        registration_stage = stage_model.search([('name', '=', 'Registration')], limit=1)
        for order in self:
            if not order.project_id:
                project = self.env['project.project'].create({
                    'name': f"{order.partner_id.name}  {order.name}",
                    'partner_id': order.partner_id.id,
                    'stage_id': registration_stage.id if registration_stage else False,
                })
                order.project_id = project.id
