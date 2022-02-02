/** @odoo-module **/

import {_t} from 'web.core';
import {Markup} from 'web.utils';
import tour from 'web_tour.tour';

tour.register('rental_tour', {
    url: "/web",
    rainbowManMessage: _t("Congrats, the first your car just created! :)"),
    sequence: 10,
},
    [tour.stepUtils.showAppsMenuItem(), {
    trigger: '.o_app[data-menu-xmlid="rental.menu_root"]',
    content: Markup(_t('Ready to create new car?')),
    position: 'bottom',
}, {
    trigger: '.dropdown-toggle[data-menu-xmlid="rental.configuration"]',
    content: Markup(_t('Please open <b>Configuration</b>.')),
    position: 'bottom',
}, {
    trigger: '.dropdown-item[data-menu-xmlid="rental.menu_car_info"]',
    content: Markup(_t('Please open <b>Car Info</b>.')),
    position: 'right',
}, {
    trigger: 'button.o_list_button_add',
    extra_trigger: '.o_rental_car_info_tree',
    content: Markup(_t("<b>Create your first car info.</b>")),
    position: 'bottom',
}, {
    trigger: ".o_form_view .o_field_widget[name='name']",
    content: Markup(_t('Write a <b>car name</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("Opel", this.$anchor);
    }
}, {
    trigger: ".o_form_view .o_field_widget[name='model_id']",
    content: Markup(_t('Set a <b>model</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("Astra", this.$anchor.find('input'));
    }
}, {
    trigger: ".o_form_view .o_field_widget[name='country_id']",
    content: Markup(_t('Set a <b>country</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("Germany", this.$anchor.find('input'));
    }
}, {
    trigger: ".o_form_view .o_field_widget[name='description']",
    content: Markup(_t('Set a <b>description</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("The Opel Astra is a compact car/small family car...", this.$anchor.find('input'));
    }
}, {
    trigger: 'button.o_form_button_save',
    extra_trigger: '.o_rental_car_info_form',
    content: Markup(_t("<b>Save your first car info.</b>")),
    position: 'bottom',
}, {
    mobile: false,
    trigger: ".breadcrumb-item:first",
    content: Markup(_t("Use the breadcrumbs to <b>go back to products</b>.")),
    position: "bottom",
    run: function (actions) {
        actions.auto(".breadcrumb-item:not(.active):last");
    }
},
]);