/** @odoo-module **/

import { _t } from 'web.core';
import { Markup } from 'web.utils';
import tour from 'web_tour.tour';

tour.register('rental_tour', {
    url: "/web",
    rainbowManMessage: _t("Let's take a tour around! :)"),
    sequence: 10,
}, [tour.stepUtils.showAppsMenuItem(), {
    trigger: '.o_app[data-menu-xmlid="rental.car_rental_menu_root"]',
    content: Markup(_t('Let\'s have a look at your <b>Pipeline</b>.')),
    position: 'right',
    edition: 'community',
},
])