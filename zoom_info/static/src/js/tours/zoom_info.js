odoo.define('zoom_info.zoom_info_tour', function (require) {
    "use strict";

    var tour = require('web_tour.tour');

    tour.register('zoom_info_tour', {
        test: true,
        url: "/web#action=contacts.action_contacts&view_type=tree",
    }, [
        tour.stepUtils.showAppsMenuItem(),
        {
            trigger: ".o_app[data-menu-xmlid='contacts.contacts_menu_root']",
            content: "open contacts app",
        },
    {
    trigger: '.o-kanban-button-new',
    extra_trigger: '.o_res_partner_kanban',
    content: _t("<b>Create your first contact.</b>"),
    position: 'bottom',
},

// pass


        {
            trigger: "button[name=action_set_won_rainbowman]",
            content: "click button mark won",
        }, {
            trigger: ".o_menu_brand",
            extra_trigger: ".o_reward_rainbow",
            content: "last rainbowman appears",
        }
    ]);
});