/** @odoo-module **/

import { _t } from 'web.core';
import { Markup } from 'web.utils';
import tour from 'web_tour.tour';

tour.register('rental_tour', {
    url: "/web",
    rainbowManMessage: _t("Now you're up to go! :)"),
    sequence: 10,
}, [tour.stepUtils.showAppsMenuItem(), {
    trigger: '.o_app[data-menu-xmlid="rental.car_rental_menu_root"]',
    content: Markup(_t('Let\'s have a look at your <b>Pipeline</b>.')),
    position: 'right',
    edition: 'community',
}, {
    trigger: '.dropdown-toggle[data-menu-xmlid="rental.car_rental_first_level_menu"]',
    content: Markup(_t('You can choose what you want displayed on the page.')),
    position: 'bottom'
}, {
    trigger: '.dropdown-item[data-menu-xmlid="rental.display_all_models_menu_action"]',
    content: Markup(_t('Let\'s see what models are already in catalogue!')),
    position: 'right'
}
])