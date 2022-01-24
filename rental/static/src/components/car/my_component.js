odoo.define('rental.MyCustomFieldRender', function (require) {
    "use strict";

    const {Component} = owl;
    // const {useService} = owl.hooks;
    const {getData} = require('rental.services');
    const AbstractFieldOwl = require('web.AbstractFieldOwl');
    const field_registry = require('web.field_registry_owl');

    class MyCustomFieldRender extends AbstractFieldOwl {
        constructor(...args) {
            super(...args);
        }

        setup() {
            if (this.options.mode !== 'edit') {
                return;
            }
        }

        async onValueChange(ev) {
            const self = this;
            const query = ev.target.value
            const data = await getData(self, query);
            console.log(data)

            debugger;
            // self.$el.parent().find('.rental_search_div').remove();
            console.log(data)
            if (data.model_list.length > 0) {
                debugger;
                const element = $(qweb.render('rental.list_car', {
                    list_partner: data.model_list
                }));
                element.find('.o_input')
                // element.find('.rental_search_ul').on('click', self.onClickList.bind(self))
                self.$el.after(element);
            }
        }
    }

    MyCustomFieldRender.template = 'rental.MyCustomFieldRender';
    field_registry.add('my_custom_field_owl', MyCustomFieldRender);
    return MyCustomFieldRender;
});
