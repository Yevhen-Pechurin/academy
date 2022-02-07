odoo.define('zoom_info.tour', function (require) {
    "use strict";
    
    const core = require('web.core');
    const tour = require('web_tour.tour');
    
    const _t = core._t;    

    tour.register('contact_tour', {
        url: "/web#action=114&model=res.partner&view_type=kanban&cids=&menu_id=89",
        rainbowManMessage: _t("Now you're up to go! :)"),
        sequence: 10,
    }, [{
        trigger: '.o-kanban-button-new',
        extra_trigger: '.o_res_partner_kanban',
        content: _t('Create your first contact!'),
        position: 'right'
    }, {
        trigger: ".o_form_view .o_field_widget[name='name']",
        content: _t('Write your contact name!'),
        position: 'top',
        run: function(actions) {
            actions.text('Tesla', this.$anchor);
        }
    }, {
        trigger: ".zoom_search_li > span",
        auto: true,
        in_modal: false
    }, {
        trigger: '.o_form_button_save',
        extra_trigger: '.o_form_view',
        content: _t('Save your first contact.'),
        position: 'right'
    }, {
        mobile: false,
        trigger: '.breadcrumb-item:first',
        content: _t('Use the breadcrumbs to go back.'),
        position: 'bottom',
        run: function(actions) {
            actions.auto('.breadcrumb-item:not(.active)');
        }
    }
    ])

});