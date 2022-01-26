/** @odoo-module **/
const registry = require('web.field_registry_owl');

const AbstractField = require('web.AbstractFieldOwl');
const core = require('web.core');
const {tags} = owl;
const {useState} = owl.hooks;

const qweb = core.qweb;

class List extends AbstractField {
    state = useState({value: 1, 'start_value': this.props.record.data.mode, mode: 'readonly'});

    constructor(parent, value) {
        super(...arguments);
    }

    setup() {

    }

    input() {
        const self = this;
        const keys = document.getElementById("input").value;


        const data = this.env.services.rpc({
                model: 'rental.car',
                method: 'get_cars',
                args: [keys, 'model'],
            }).then(res => {
                    console.log(this.env)
                    if (res.length != 0) {
                        const element =$(self.env.qweb.render('rental.list', {
                            data: res
                        }));

                        debugger
                        self.el.after(element);
                    }


                }
            )
        ;
    }


}

List.template = 'myaddon.MyComponent';
registry.add('cringet', List)
