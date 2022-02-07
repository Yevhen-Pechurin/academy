odoo.define('zoom.tour', function (require) {

    var core = require('web.core');
    var tour = require('web_tour.tour');

    function wait(ms) {
        var start = new Date().getTime();
        var end = start;
        while (end < start + ms) {
            end = new Date().getTime();
        }
    }

    var _t = core._t;

    tour.register('zoom_tour', {
        url: "/web",
        sequence: 1,
    }, [tour.stepUtils.showAppsMenuItem(),
        {
            trigger: '.o_app[data-menu-xmlid="contacts.menu_contacts"]',
            content: _t('Let`s create new <b>Contact</b>.'),
            position: 'bottom',
        },
        {
            trigger: '.o-kanban-button-new',

            content: _t("<b>Create your first Contact</b>"),
            position: 'bottom',
        },
        {
            trigger: ".o_field_widget[name='name']",
            content: _t('<b>Write contact name</b>.'),
            position: "top",
            run: function (actions) {
                actions.text("Tesla", this.$anchor);

            },
        },
        {
            trigger: ".zoom_search_ul .list_person_span",
            content: _t('<b>click</b>.'),
            position: "top",
            run: function (actions) {
                wait(500);
                actions.click(this.$anchor);
            },
        },

        {
            trigger: '.o_form_button_save',
            content: _t("<b>Let`s save your new contact.</b>"),
            position: 'bottom',
        },
        {
            mobile: false,
            trigger: '.breadcrumb-item:first',
            content: _t("<b>End.</b>"),
            run: function (actions) {
                actions.auto(".breadcrumb-item:not(.active):last")
            }
        }
    ]);
});