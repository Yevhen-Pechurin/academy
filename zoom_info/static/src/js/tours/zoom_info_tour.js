odoo.define('zoom_info.tour', function(require) {
"use strict";

var core = require('web.core');
var tour = require('web_tour.tour');
var _t = core._t;

tour.register("zoom_info_tour", {
    url: "/web",
    rainbowManMessage: _t("Let's check your new module"),
    sequence: 20,
}, [tour.stepUtils.showAppsMenuItem(), {
    trigger: ".o_app[data-menu-xmlid='contacts.menu_contacts']",
    content: _t("Open Contacts app to test Zoom module"),
    position: "right",
    edition: "community"
}, {
    trigger: '.o-kanban-button-new',
    extra_trigger: '.o_res_partner_kanban',
    content: _t("<b>Create your first contact.</b>"),
    position: 'bottom',
}, {
    trigger: ".o_form_view .o_field_widget[name='name']",
    content: _t('Write a <b>Contact name</b>'),
    position: "top",
    run: function (actions) {
        actions.text("Tesla", this.$anchor);
    }
}, {
        trigger: ".zoom_search_li > span",
        auto: true,
        in_modal: false
}, {
    trigger: 'button.o_form_button_save',
    extra_trigger: '.o_form_sheet_bg',
    content: _t("<b>Save your first car</b>"),
    position: 'bottom',
}, {
    trigger: ".breadcrumb-item:not(.active):first",
    content: _t("Click on the breadcrumb to go back to the Pipeline."),
    position: "bottom",
    run: function (actions) {
        actions.auto(".breadcrumb-item:not(.active):last");
    }
},
]);
});