/** @odoo-module **/

import { _t } from 'web.core';
import { Markup } from 'web.utils';
import tour from 'web_tour.tour';

tour.register('rental_tour', {
    url: "/web",
    rainbowManMessage: _t("Congrats, best of luck catching such big fish! :)"),
    sequence: 10,
}, [tour.stepUtils.showAppsMenuItem(), {
    trigger: '.o_app[data-menu-xmlid="rental.menu_root"]',
    content: Markup(_t('Ready to create your car?')),
    position: 'bottom',
}, {
    trigger: '.dropdown-toggle[data-menu-xmlid="rental.menu_rental"]',
    content: Markup(_t('Please open<b>Rental</b>.')),
    position: 'bottom',
}, {
    trigger: '.dropdown-item[data-menu-xmlid="rental.menu_all_cars"]',
    content: Markup(_t('Please open<b>Cars</b>.')),
    position: 'bottom',
}, {
    trigger: '.o_list_button_add',
    extra_trigger: '.o_rental_car_view_tree',
    content: Markup(_t("<b>Create your first car.</b>")),
    position: 'bottom',
}, {
    trigger: ".o_form_view .o_field_widget[name='model']",
    content: Markup(_t('Write a<b>Model name</b>')),
    position: "top",
    run: function (actions) {
        actions.text("Mercedes", this.$anchor);
    }
}, {
    trigger: ".o_form_view .o_field_widget[name='year']",
    content: Markup(_t('Write a<b>Year</b>')),
    position: "top",
    run: function (actions) {
        actions.text("2023", this.$anchor);
    }
}, {
    trigger: ".o_form_view .o_field_widget[name='odometer']",
    content: Markup(_t('Write <b>Odometer</b>')),
    position: "top",
    run: function (actions) {
        actions.text("10200", this.$anchor);
    }
}, {
    trigger: 'button.o_form_button_save',
    extra_trigger: '.o_rental_car_form',
    content: Markup(_t("<b>Save your first car</b>")),
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
