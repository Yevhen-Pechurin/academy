odoo.define('rental_car.tour', function(require) {
"use strict";

var core = require('web.core');
var tour = require('web_tour.tour');

var _t = core._t;

tour.register('rental_car_tour', {
    url: "/web",
    rainbowManMessage: _t("Congrats, best of luck catching such big fish! :)"),
    sequence: 10,
}, [tour.stepUtils.showAppsMenuItem(),
    {
    trigger: '.o_app[data-menu-xmlid="rental_car.menu_root"]',
    content: _t('Ready to create your car? Let\'s have a look at your <b>Pipeline</b>.'),
    position: 'bottom',
    edition: 'community',
},
    {
    trigger: '.o_nav_entry[data-menu-xmlid="rental_car.model"]',
    content: _t('First, u should create car model, that u need. Let\'s have a look at your <b>Pipeline</b>.'),
    position: 'right',
    edition: 'community',
},{
    trigger: 'button.o_list_button_add',
    extra_trigger: '.o_create_button',
    content: _t('Click to create your first model.'),
    position: 'bottom',
    edition: 'community',
}, {
    trigger: '.o_form_view .o_field_widget[name = "name"]',
    content: _t('Write model name'),
    position: 'bottom',
    run: function (actions) {
        actions.text("M5", this.$anchor);
    },
}, {
    trigger: '.o_form_view .o_field_widget[name = "year_of_manufacture"]',
    content: _t('Write model year'),
    position: 'bottom',
    run: function (actions) {
        actions.text("2010", this.$anchor);
    },
},{
    trigger: '.button.o_form_button_save',
    extra_trigger: '.o_model_save',
    content: _t('Save your model'),
    position: 'bottom',
}, {
    trigger: '.o_back_button',
    extra_trigger: '.o_model_save',
    content: _t('Save your model'),
    position: 'bottom',
},{
        mobile: false,
        trigger: ".breadcrumb-item:first",
        content: _t("Back to your models"),
        position: "bottom",
        run: function (actions) {
            actions.auto(".breadcrumb-item:not(.active):last");
        }
},
//     {
//     trigger: ".ui-menu-item > a",
//     auto: true,
//     in_modal: false,
// },
]);
})


