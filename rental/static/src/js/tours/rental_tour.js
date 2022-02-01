/** @odoo-module **/

import {_t} from 'web.core';
import {Markup} from 'web.utils';
import tour from 'web_tour.tour';

function openCarsFilter() {
    return {
        trigger: '.dropdown-toggle[data-menu-xmlid="rental.cars"]',
        content: Markup(_t("<b>Lets check filters for your car</b>")),
        position: 'right',
    }
}

function showFilterCar(xmlid, text) {
    return {
        trigger: `.dropdown-item[data-menu-xmlid="${xmlid}"]`,
        content: Markup(_t(text)),
        position: 'right',
    }
}
function showStatusBarCar(xmlid, text) {
    return {
        trigger: `.o_field_widget [data-value="${xmlid}"]`,
        content: Markup(_t(text)),
        position: 'bottom',
        run: function (actions) {
            actions.click();
        }
    }
}

tour.register('rental_tour', {
    url: "/web",
    rainbowManMessage: _t("In the game you can drive without any rules, but in real life, be careful on the road...and fasten your seatbelt! ;)"),
    sequence: 10,
}, [tour.stepUtils.showAppsMenuItem(), {
    trigger: '.o_app[data-menu-xmlid="rental.car_rental_menu"]',
    content: Markup(_t('Ready to boost your sales? Let\'s have a look at your <b>Pipeline</b>.')),
    position: 'bottom',
},
    openCarsFilter(),
    showFilterCar("rental.unavailable_cars", '<b>Here you can see all your iron horses which not be able to be rented</b>'),
    openCarsFilter(),
    showFilterCar("rental.repair_cars", '<b>Here you can see all your iron horses which fells unhealthy</b>'),
    openCarsFilter(),
    showFilterCar("rental.loan_cars", '<b>Here you can see all your iron horses which are using others people</b>'),
    openCarsFilter(),
    showFilterCar("rental.garage_cars", '<b>Here you can see your iron horses which are slepping in their house</b>'),
    openCarsFilter(),
    showFilterCar("rental.all_cars", '<b>Here you can see all your iron horse</b>'),
    {
        trigger: '.o_list_button_add',
        content: Markup(_t("<b>Lets add record with your car.</b>")),
        position: 'bottom',
        run: function (actions) {
            actions.click();
        }
    },
    showStatusBarCar('on_loan', '<b>Here you can choose/change status of your car</b>'),
    showStatusBarCar('under_repair', '<b>Here you can choose/change status of your car</b>'),
    showStatusBarCar('unavailable', '<b>Here you can choose/change status of your car</b>'),

    {
        trigger: '.o_field_widget[name="model"]',
        content: Markup(_t("Here input model your car. Like:<b>Jetta</b>")),
        position: 'bottom',
        run: function (actions) {
            actions.text("Jetta", this.$anchor)
        }
    },{
        trigger: '.o_field_widget[name="number"]',
        content: Markup(_t("Here input number your car. Like:<b>301718</b>")),
        position: 'bottom',
        run: function (actions) {
            actions.text(301718, this.$anchor)
        }
    }, {
        trigger: '.o_datepicker_input[name="year"]',
        content: Markup(_t("Here input year your car. Like:<b>02/01/2022</b>")),
        position: 'bottom',
        run: function (actions) {
            actions.text('02/01/2022', this.$anchor)
        }
    }, {
        trigger: '.o_field_widget[name="odometer"]',
        content: Markup(_t("Here input odometer your car. Like:<b>228228</b>")),
        position: 'bottom',
        run: function (actions) {
            actions.text(228228, this.$anchor)
        }
    },
    {
        trigger: '.o_form_button_save',
        content: Markup(_t("<b>Lets save our changes.</b>")),
        position: 'bottom',
        run: function (actions) {
            actions.click();
        }
    },{
        trigger: '.loan_history',
        content: Markup(_t("Here will show information of history about your car</b>")),
        position: 'top',
        run: function (actions) {actions.click();}
    },{
        trigger: '.repair_history',
        content: Markup(_t("Here will show information of repair your car</b>")),
        position: 'top',
        run: function (actions) {actions.click();}
    }, {
        trigger: '.o_MessageList_separator',
        content: Markup(_t("Here will show messages of processes in module</b>")),
        position: 'top',

    }

]);