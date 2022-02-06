/** @odoo-module **/

import {_t} from 'web.core';
import {Markup} from 'web.utils';
import tour from 'web_tour.tour';

tour.register('demo_tour', {
    url: "/web",
    rainbowManMessage: _t("Congrats, best of luck catching such big fish! :)"),
    sequence: 10,
}, [tour.stepUtils.showAppsMenuItem(), {
    trigger: '.o_app[data-menu-xmlid="demo.menu_root"]',
    content: Markup(_t('Ready to create new demo?')),
    position: 'bottom',
}, {
    trigger: '.dropdown-toggle[data-menu-xmlid="demo.demo"]',
    content: Markup(_t('Please open <b>Demo</b>.')),
    position: 'bottom',
}, {
    trigger: '.dropdown-item[data-menu-xmlid="demo.menu_demo"]',
    content: Markup(_t('Please open <b>All Demos</b>.')),
    position: 'right',
}, {
    trigger: '.o-kanban-button-new',
    content: Markup(_t("<b>Create your first demo.</b>")),
    position: 'bottom',
}, {
    trigger: ".o_form_view .o_field_widget[name='partner_id']",
    content: Markup(_t('Write a <b>client`s name</b>.')),
    position: "bottom",
    run: function (actions) {
        actions.text("Brandon Freeman", this.$anchor.find('input'));
    }
}, {
    trigger: ".ui-menu-item > a",
    auto: true,
    in_modal: false,
}, {
    trigger: ".o_field_widget[name='partner_id'] input",
    auto: true,
    run: function () {
    }                 // wait for the creation
}, {
    trigger: ".o_form_view .o_field_widget[name='date']",
    content: Markup(_t('Set a <b>date</b> of demo.')),
    position: "bottom",
    run: function (actions) {
        actions.text("02/25/2022", this.$anchor.find('input'));
    }
}, {
    trigger: ".ui-menu-item > a",
    auto: true,
    in_modal: false,
},{
    trigger: ".o_field_widget[name='date'] input",
    auto: true,
    run: function () {
    }                 // wait for the creation
}, {
    trigger: ".o_form_view .o_field_widget[name='state_id']",
    content: Markup(_t('Set a <b>state</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("Scheduled", this.$anchor.find('input'));
    }
}, {
    trigger: ".ui-menu-item > a",
    auto: true,
    in_modal: false,
},{
    trigger: ".o_field_widget[name='state_id'] input",
    auto: true,
    run: function () {
    }                 // wait for the tag creation
}, {
    trigger: ".o_form_view textarea.o_field_widget",
    content: Markup(_t('Set a <b>description</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("Test our new product...", this.$anchor);
    }
},{
    trigger: ".o_form_view textarea.o_field_widget",
    auto: true,
    run: function () {
    }                 // wait for the creation
}, {
    trigger: 'button.o_form_button_save',
    extra_trigger: '.o_demo_demo_form',
    content: Markup(_t("<b>Save your first demo.</b>")),
    position: 'bottom',

}, {
    mobile: false,
    trigger: ".breadcrumb-item:first",
    content: Markup(_t("Use the breadcrumbs to <b>go back to demos</b>.")),
    position: "bottom",
    run: function (actions) {
        actions.auto(".breadcrumb-item:not(.active):last");
    }
},
]);