from odoo import models, _
from odoo.exceptions import AccessError

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def write(self, vals):

        if self.env.user.has_group('project_access_solar.project_access_all'):
            return super().write(vals)

        # Define access of group
        group_access = {
            'project_access_solar.project_access_person1': {
                'allowed_fields': [
                    'application_date', 'application_number', 'discom_name',
                    'feasibility_approved_date', 'consumer_aadharcard', 'consumer_pan',
                    'consumer_electricity_bill', 'consumer_taxbill', 'application_letter',
                    'feasibility_letter'
                ],
                'allowed_stages': ['Registration', 'Application', 'Feasibility', 'Vendor Selection'],
            },

            'project_access_solar.project_access_person2': {
                'allowed_fields': ['estimate_no', 'estimate_status', 'estimate_paid_receipt'],
                'allowed_stages': [],
            },

            'project_access_solar.project_access_person3': {
                'allowed_fields': [],
                'allowed_stages': [],
            },

            'project_access_solar.project_access_person4': {
                'allowed_fields': ['agreement_discom', 'model_agreement_pdf'],
                'allowed_stages': ['Upload Agreement', 'Installation'],
            },

            'project_access_solar.project_access_person5': {
                'allowed_fields': [],
                'allowed_stages': ['Project Commissioning', 'Subsidy Request', 'Subsidy Disbursal'],
            },
        }

        # Check which group user belongs to
        for group, access in group_access.items():
            if self.env.user.has_group(group):
                # Stage check
                if 'stage_id' in vals:
                    stage = self.env['project.task.type'].browse(vals['stage_id']).name
                    if access['allowed_stages'] and stage not in access['allowed_stages']:
                        raise AccessError(_("You are not allowed to move to this stage."))

                    if not access['allowed_stages']:
                        raise AccessError(_("You are not allowed to change the stage."))

                # Field check
                for field in vals:
                    if field != 'stage_id' and field not in access['allowed_fields']:
                        raise AccessError(_("You are not allowed to change this field."))

                return super().write(vals)

        raise AccessError(_("You do not have access to update this task."))
