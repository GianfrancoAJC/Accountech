<template>
    <h1>Inventory Page</h1>
    <br>
    <button @click="fetchInventories">Inventorario</button>
    <h1>{{inventories.length}}</h1>
    <div v-if="inventories.length">
        <table class="inventory-table">
            <tr>
                <th>ID</th>
                <th>PRODUCT_ID</th>
                <th>QUANTITY</th>
                <th>AMOUNT</th>
                <th>EMPLOYEE_ID</th>
                <th>CREATED_AT</th>
                <th>MODIFIED_AT</th>
            </tr>
            <tr v-for="inventory in inventories" :key="inventory.id">
                <td>{{ inventory.id }}</td>
                <td>{{ inventory.product_id }}</td>
                <td>{{ inventory.quantity }}</td>
                <td>{{ inventory.amount }}</td>
                <td>{{ inventory.employee_id }}</td>
                <td>{{ inventory.created_at }}</td>
                <td>{{ inventory.modified_at }}</td>
            </tr>
        </table>
    </div>
    <div v-else>
        <h1>Loading jobs...</h1>
    </div>
    <br>
</template>

<script>

import { getinventory } from '@/services/inventory.api';

export default {
    data() {
        return {
            inventories: [],
        }
    },
    methods: {
        async fetchInventories() {
            const { products } = await getinventory();
            console.log('products: ', products, typeof(products));
            for (let i = 0; i < products.length; i++) {
                this.inventories.push(products[i]);
            }
            console.log('inventories: ', this.inventories, typeof(this.inventories));
        }
    }
}
</script>

<style>
.inventory-table {
    font-family: Arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

.inventory-table th,
.inventory-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

.inventory-table th {
    background-color: #f2f2f2;
}

.inventory-table td:first-child {
    font-weight: bold;
}

.inventory-table td:nth-child(n+4) {
    text-align: right;
}

.inventory-table tr:nth-child(even) {
    background-color: #f9f9f9;
}
</style>
