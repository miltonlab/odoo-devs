openerp.siscop = function(instance) {
    var _t = instance.web._t;
    var _lt = instance.web.qweb;

    instance.siscop = {};

    instance.siscop.HomePage = instance.web.Widget.extend({
	start: function() {
	    console.log('Starting SISCOP oeweb module');
	    alert('playing...');
	},
    });
    instance.web.client_actions.add('siscop.homepage', 
				    'instance.siscop.HomePage');
    
}
