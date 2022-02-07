odoo.define('zoom_info.tour', function(require) {
"use strict";

var core = require('web.core');
var tour = require('web_tour.tour');

var _t = core._t;

tour.register('zoom_info_tour', {
    url: "/web#action=114&model=res.partner&view_type=kanban&cids=&menu_id=89",
    rainbowManMessage: _t("Congrats, best of luck catching such big fish! :)"),
    sequence: 10,
}, [tour.stepUtils.showAppsMenuItem(),
    {
    trigger: 'button.o-kanban-button-new',
    extra_trigger: '.o_res_partner_kanban',
    content: _t('Click to create your first model.'),
    position: 'bottom',
    edition: 'community',
}, {
    trigger: '.o_form_view .o_form_sheet_bg .o_field_widget[name = "name"]',
    content: _t('Write company name'),
    position: 'bottom',
    run: function (actions) {
        actions.text("Tesla", this.$anchor);
    },
},{
    trigger: '.o_form_view .o_form_sheet_bg .zoom_search_div .list-unstyled .zoom_search_li .list_person_span',
    content: _t('Write company name'),
    position: 'bottom',
    run: function (actions) {
        actions.click();
        $('span.list_person_span input[type="text"]').val('Tesla');
    },
},
// {
//     trigger: '.o_form_view .o_field_widget[name = "year_of_manufacture"]',
//     content: _t('Write model year'),
//     position: 'bottom',
//     run: function (actions) {
//         actions.text("2010", this.$anchor);
//     },
// },{
//     trigger: '.button.o_form_button_save',
//     extra_trigger: '.o_model_save',
//     content: _t('Save your model'),
//     position: 'bottom',
// }, {
//     trigger: '.o_back_button',
//     extra_trigger: '.o_model_save',
//     content: _t('Save your model'),
//     position: 'bottom',
// },{
//         mobile: false,
//         trigger: ".breadcrumb-item:first",
//         content: _t("Back to your models"),
//         position: "bottom",
//         run: function (actions) {
//             actions.auto(".breadcrumb-item:not(.active):last");
//         }
// },
//     {
//     trigger: ".ui-menu-item > a",
//     auto: true,
//     in_modal: false,
// },
]);
})


