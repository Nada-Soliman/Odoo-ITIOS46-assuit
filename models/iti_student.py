from odoo import models, fields, api

class ITIStudent(models.Model):
    _name = 'iti.student'

    # _rec_name = 'age'

    name = fields.Char()
    age = fields.Integer()
    info = fields.Text()
    is_accepted = fields.Boolean()
    birth_date = fields.Date()
    image = fields.Binary()
    gender = fields.Selection([('female','F'),('male','M')])

    salary = fields.Float("")
    is_working = fields.Boolean("")
    cv = fields.Html()

    track_id = fields.Many2one('iti.track')
    track_capacity =  fields.Integer(related='track_id.capacity')

    @api.onchange('is_working')
    def _onchange_is_working(self):
        if self.is_working:
            self.salary = 10000
        else:
            self.salary = 0

        return {
            'warning': {
                'title': ('State Changed'),
                'message': 'Working state is changed to %s' %(self.is_working)
            }}

    def confirm_action(self):
        self.is_accepted = True
        print("in confirm_action")
