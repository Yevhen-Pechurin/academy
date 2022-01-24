odoo.define('rental.MyCustomFieldRender', function (require) {
    "use strict";

    const {Component} = owl;
    const {useState} = owl.hooks;
    const AbstractFieldOwl = require('web.AbstractFieldOwl');
    const field_registry = require('web.field_registry_owl');

// class ChangeLine extends Component { }
// ChangeLine.template = 'rental.ResequenceChangeLine';
// ChangeLine.props = ["changeLine", 'ordering'];


    class MyCustomFieldRender extends AbstractFieldOwl {
        constructor(...args) {
            super(...args);
            // debugger
            // this.data = this.value ? JSON.parse(this.value) : {
            //     changeLines: [],
            //     ordering: 'date',
            // };
        }
        setup() {
            // this.
            if(this.options.mode !== 'edit'){
                return;
            }
            // debugger;
        }

        // willstart (){
        //     debugger;
        // }
        // async willUpdateProps(nextProps) {
        //     await super.willUpdateProps(nextProps);
        //     Object.assign(this.data, JSON.parse(this.value));
        // }
        // _onKeydown(ev) {
        //     switch (ev.which) {
        //         // Trigger only if the user clicks on ENTER or on TAB.
        //         case $.ui.keyCode.ENTER:
        //             console.log('111')
        //         case $.ui.keyCode.TAB:
        //             // trigger blur to prevent the code being executed twice
        //             $(ev.target).blur();
        //     }
        // }

        onValueChange(ev) {
            console.log('1111')

            const self = this;

            // const query = this.$el.val()
            const query = ev.target.value
            debugger;
            this._rpc({
                model: 'rental.car',
                method: 'get_model',
                args: [query],
            }).then((data) => {
                self.$el.parent().find('.rental_search_div').remove();
                if (data.model_list.length > 0) {
                    const element = $(qweb.render('rental.list_car', {
                        list_partner: data.model_list
                    }));
                    element.find('.rental_search_ul').on('click', self.onClickList.bind(self))
                    self.$el.after(element);

                }
            })
        }
    }

    MyCustomFieldRender.template = 'rental.MyCustomFieldRender';
// MyCustomFieldRender.components = { ChangeLine }

    field_registry.add('my_custom_field_owl', MyCustomFieldRender);
    return MyCustomFieldRender;
});
