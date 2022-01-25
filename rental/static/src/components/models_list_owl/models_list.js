/** @odoo-module alias=rental.models_list_owl **/
"use strict";

const { Component } = owl;
const { useState } = owl.hooks;
//const { xml } = owl.tags;   //static template = xml``;
const AbstractFieldOwl = require('web.AbstractFieldOwl');
const field_registry = require('web.field_registry_owl');
import { useService } from "@web/core/utils/hooks";

class Parent extends AbstractFieldOwl {
    setup() {
        this.rpc = useService("rpc");
        this.state = useState({models: []});
    };

    async _onInput(ev) {
        if (ev.target.value === '') { this.state.models = []; return; };
        this.state.models = await this.rpc({
            model: 'rental.car', 
            method: 'get_model',
            args: [ev.target.value]});
    };

    async _onClickGetModelInfo(ev) {
        const {model_name: model, manufacturer_logo: logo} = (await this.rpc({
            model: 'rental.car_model',
            method: 'read',
            args: [[+ev.target.dataset.id], ['model_name', 'manufacturer_logo']],
            }))[0];
        this.trigger('field-changed', {
            dataPointID: this.dataPointId,
            changes: {model, logo},
        });
        ev.target.parentElement.parentElement.previousSibling.value = model;
        this.state.models = [];
        ev.stopPropagation();
    };

    async _onFocusoutCleanup() {
        //setTimeout is essential here to prevent dropdown list being deleted before ul click event can take place
        setTimeout(() => {
            this.state.models = [];
        }, 200);
        
    };
}
Parent.template = 'rental.ModelsListComponent';

field_registry.add('custom-component-wrapper', Parent);

export default Parent;