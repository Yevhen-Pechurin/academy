/** @odoo-module **/

import {_t} from 'web.core';
import {Markup} from 'web.utils';
import tour from 'web_tour.tour';

tour.register('rental_tour', {
    url: "/web",
    rainbowManMessage: _t("Congrats, best of luck catching such big fish! :)"),
    sequence: 1,
}, [tour.stepUtils.showAppsMenuItem(),
    {
        trigger: '.o-dropdown',
        content: Markup(_t('Let`s start <b>Car</b>.')),
        position: 'bottom',
    }, {
        trigger: '.o_app[data-menu-xmlid="rental.car_rental_menu"]',
        content: Markup(_t('Let`s create new <b>Car</b>.')),
        position: 'bottom',
    },
    {
        trigger: '.o_list_button_add',
        extra_trigger: '.car_tree_view',
        content: Markup(_t("<b>Create your first car</b>")),
        position: 'bottom',
    },
    {
        trigger: ".o_form_view .o_field_widget[name='model']",
        content: Markup(_t('<b>Write car model</b>.')),
        position: "top",
        run: function (actions) {
            actions.text("Aston Martin", this.$anchor);
        },
    },
    {
        trigger: ".o_form_view .o_field_widget[name='number']",
        content: Markup(_t('<b>Write car number</b>.')),
        position: "top",
        run: function (actions) {
            actions.text(11, this.$anchor);
        },
    },
    {
        trigger: '.btn-primary[name="action_loan"]',
        content: Markup(_t("<b>Click Loan button/b>")),
        position: 'bottom',
    },
    {
        trigger: ".o_field_widget[name='partner_id']",
        content: Markup(_t('<b>Write car partner</b>.')),
        position: "top",
        run: function (actions) {
            actions.text('Azure Interior', this.$anchor.find('input'));
        },
    },
    {
        trigger: ".datetimepicker-input",
        content: Markup(_t('<b>Sa</b>.')),
        position: "top",
        run: function (actions) {
            actions.text('02/24/2022', this.$anchor);
        },
    },
    {
        trigger: '.btn-primary',
        content: Markup(_t("<b>End.</b>")),
        position: 'bottom',
    },
    {
        trigger: '.o_form_button_save',
        extra_trigger: '.car_form_view',
        content: Markup(_t("<b>Let`s save your new car.</b>")),
        position: 'bottom',
    },
    {
        mobile: false,
        trigger: '.breadcrumb-item:first',
        content: Markup(_t("<b>End.</b>")),
        run: function (actions) {
            actions.auto(".breadcrumb-item:not(.active):last")
        }
    }
]);
