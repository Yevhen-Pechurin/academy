/** @odoo-module **/

import {_t} from 'web.core';
import {Markup} from 'web.utils';
import tour from 'web_tour.tour';

tour.register('library_tour', {
    url: "/web",
    rainbowManMessage: _t("Congrats, you have just created your first book info! :)"),
    sequence: 10,
},
    [tour.stepUtils.showAppsMenuItem(), {
    trigger: '.o_app[data-menu-xmlid="library.menu_root"]',
    content: Markup(_t('Ready to create new book?')),
    position: 'bottom',
}, {
    trigger: '.dropdown-toggle[data-menu-xmlid="library.configuration"]',
    content: Markup(_t('Please open <b>configuration</b>.')),
    position: 'bottom',
}, {
    trigger: '.dropdown-item[data-menu-xmlid="library.menu_book_info"]',
    content: Markup(_t('Please open <b>Book Info</b>.')),
    position: 'right',
}, {
    trigger: 'button.o_list_button_add',
    extra_trigger: '.o_library_book_info_tree',
    content: Markup(_t("<b>Create your first book info.</b>")),
    position: 'bottom',
}, {
    trigger: ".o_form_view .o_field_widget[name='name']",
    content: Markup(_t('Write a <b>books name</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("Harry Potter", this.$anchor);
    }
}, {
    trigger: ".o_form_view .o_field_widget[name='author_id']",
    content: Markup(_t('Set a <b>author</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("J. K. Rowling", this.$anchor.find('input'));
    }
}, {
    trigger: ".ui-menu-item > a",
    auto: true,
    in_modal: false,
},{
    trigger: ".o_field_widget[name='author_id'] input",
    auto: true,
    run: function () {
    }                 // wait for the tag creation
},{
    trigger: ".o_form_view .o_field_widget[name='lang_id']",
    content: Markup(_t('Set a <b>language</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("English", this.$anchor.find('input'));
    }
}, {
    trigger: ".ui-menu-item > a",
    auto: true,
    in_modal: false,
},{
    trigger: ".o_field_widget[name='lang_id'] input",
    auto: true,
    run: function () {
    }                 // wait for the tag creation
},{
    trigger: ".o_form_view .o_field_widget[name='tag_ids']",
    content: Markup(_t('Add <b>tags</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("Fantasy", this.$anchor.find('input'));
    }
}, {
    trigger: ".ui-menu-item > a",
    auto: true,
    in_modal: false,
}, {
    trigger: ".o_badge_text[title='Fantasy']",
    auto: true,
    run: function () {
    }                 // wait for the tag creation
}, {
    trigger: ".o_form_view .o_field_widget[name='tag_ids']",
    content: Markup(_t('Add one more <b>tags</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("Adventures", this.$anchor.find('input'));
    }
}, {
    trigger: ".ui-menu-item > a",
    auto: true,
    in_modal: false,
}, {
    trigger: ".o_badge_text[title='Adventures']",
    auto: true,
    run: function () {
    }                 // wait for the tag creation
}, {
    trigger: ".o_form_view textarea.o_field_widget",
    content: Markup(_t('Set a <b>description</b>')),
    position: "bottom",
    run: function (actions) {
        actions.text("Dark times have come to Hogwarts...", this.$anchor);
    }
},{
    trigger: ".o_form_view textarea.o_field_widget",
    auto: true,
    run: function () {
    }                 // wait for the tag creation
},{
    trigger: 'button.o_form_button_save',
    extra_trigger: '.o_library_book_info_form',
    content: Markup(_t("<b>Save your first book info.</b>")),
    position: 'bottom',
}, {
    mobile: false,
    trigger: ".breadcrumb-item:first",
    content: Markup(_t("Use the breadcrumbs to <b>go back to books</b>.")),
    position: "bottom",
    run: function (actions) {
        actions.auto(".breadcrumb-item:not(.active):last");
    }
},
]);