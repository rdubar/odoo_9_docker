# Dietfacts application
from openerp import models, fields, api

# Extend product.template model with calories

class DietFacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer("Calories")
    servingsize = fields.Float('Serving Size')
    lastupdated = fields.Date('Last Updated')
    nutrient_ids = fields.One2many('product.template.nutrient','product_id','Nutrients')
    
    @api.one
    @api.depends('nutrient_ids','nutrient_ids.value')
    def _calcscore(self):
        currentscore = 0
        for nutrient in self.nutrient_ids:
            if nutrient.nutrient_id.name == 'Sodium':
                currentscore = currentscore + (nutrient.value / 5)
            if nutrient.nutrient_id.name == 'Fat':
                currentscore = currentscore - (nutrient.value / 10)
        self.nutrition_score = currentscore
    nutrition_score = fields.Float(string="Nutrition Score", store=True, compute="_calcscore")
    
class DietFacts_res_users_meal(models.Model):
    _name = 'res.users.meal'
    name = fields.Char("Meal Name")
    meal_date = fields.Datetime("Meal Date")
    item_ids = fields.One2many('res.users.mealitem','meal_id')
    user_id = fields.Many2one('res.users','Meal User')
    largemeal = fields.Boolean("Large Meal")
    
    @api.onchange('totalcalories')
    def check_totalcalories(self):
        if self.totalcalories > 500:
            self.largemeal = True
        else:
            self.largemeal = False
             
    @api.one
    @api.depends('item_ids','item_ids.servings')
    def _calccalories(self):
        currentcalories = 0
        for mealitem in self.item_ids:
            currentcalories = currentcalories + (mealitem.calories * mealitem.servings)
        self.totalcalories = currentcalories
       
    totalcalories = fields.Integer(string="Total Meal Calories", store=True, compute="_calccalories")
    notes = fields.Text('Meal Notes')
    
class DietFacts_res_users_mealitem(models.Model):
    _name = 'res.users.mealitem'
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template','Meal Item')
    servings = fields.Float('Servings')
    calories = fields.Integer(related='item_id.calories', string = "Calories Per Serving", store=True, readonly=True)
    notes = fields.Text("Meal item notes")

class DietFacts_product_nutrient(models.Model):
    _name = 'product.nutrient'
    name = fields.Char("Nutrient Name")
    uom_id = fields.Many2one('product.uom','Unit of Measure')
    description = fields.Text("Description")
    
class DietFacts_product_template_nutrient(models.Model):
    _name = 'product.template.nutrient'
    nutrient_id = fields.Many2one('product.nutrient',string="Product Nutrient")
    product_id = fields.Many2one('product.template')
    uom = fields.Char(related='nutrient_id.uom_id.name', string = "UOM", readyonly=True)
    value = fields.Float('Nutrient Value')
    dailypercent = fields.Float("Daily Recommended Value")
    
    

    
    
    