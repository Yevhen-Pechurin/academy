/** @odoo-module **/

const {Component, useState, mount} = owl;
const {xml} = owl.tags;
const AbstractField = require('web.AbstractFieldOwl')
var field_registry = require('web.field_registry_owl');
const Field = require('web.basic_fields_owl')
var BasicField = require('web.basic_fields').FieldChar
var core = require('web.core');
// var QWeb = core.qweb;
const qweb = new owl.QWeb();

var CharMixin = BasicField.extend({})


class MyComponent extends AbstractField {
    constructor(...args) {
        super(...args);
    }

    async _onInput(ev) {
        const self = this;
        const query = ev.target.value
        const data = await self.rpc({
            args: [query],
            method: 'brand_list',
            model: 'rental_car.car',
        }).then((data) => {
            if(data && data.length>=0){
                var elem = (qweb.render('rental_car.list', {
                        list_brand: data,


                    }));
            }


        })


    }
}



MyComponent.template = 'rental_car.brand_list';

field_registry.add('my_component_widget', MyComponent);
return MyComponent;