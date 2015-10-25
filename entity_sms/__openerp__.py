{
    'name': "Entity SMS",
    'version': "2.7",
    'author': "Sythil",
    'category': "Tools",
    'summary': "Allows 2 way sms conversations between leads/partners using the twilio gateway",
    'data': [
        'ir.cron.csv',
        'esms_core.xml',
        'res_partner.xml',
        'crm_lead.xml',
        'esms_accounts.xml',
        'esms_templates.xml',
        'esms_import.xml',
        'esms_compose.xml',
        'esms_mass_sms.xml',
        'esms_compose_multi.xml',
        'esms_autoresponse.xml',
        'esms_verified_numbers.xml',
        'esms_history.xml',
        'esms.gateways.csv',
	'security/ir.model.access.csv',
	'res.country.csv',
	'smsgateway/gateway_config.xml',
        'smsglobal/gateway_config.xml',
        'twilio/gateway_config.xml',
    ],
    'demo': [],
    'depends': ['web', 'crm','marketing'],
    'installable': True,
}