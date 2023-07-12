<template>
    <h1>Tools Page</h1>
    <br>
    <button @click="InitInventories">Init Inventory</button>
    <button @click="fetchInventories">Update Inventory</button>
    <div v-if="inventories.length">
        <h1>Inventory</h1>
        <table class="inventory-table">
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>STOCK</th>
                <th>CVU</th>
                <th>PVU</th>
            </tr>
            <tr v-for="inventory in inventories" :key="inventory.id">
                <td>{{ inventory.id }}</td>
                <td>{{ inventory.name }}</td>
                <td>{{ inventory.stock }}</td>
                <td>{{ inventory.CVu }}</td>
                <td>{{ inventory.PVu }}</td>
            </tr>
        </table>
    </div>
    <div v-else>
        <h1>Loading jobs...</h1>
    </div>
    <br>
    <div>
        <h1>Purchases</h1>
        <table class="inventory-table">
            <tr>
                <th>ID</th>
                <th>PRODUCT_ID</th>
                <th>QUANTITY</th>
                <th>AMOUNT</th>
                <th>EMPLOYEE_ID</th>
            </tr>
            <tr v-for="purchase in purchases" :key="purchase.id">
                <td>{{ purchase.id }}</td>
                <td>{{ purchase.product_id }}</td>
                <td>{{ purchase.quantity }}</td>
                <td>{{ purchase.amount }}</td>
                <td>{{ purchase.employee_id }}</td>
            </tr>
        </table>
    </div>
    <div>
        <h1>Sales</h1>
        <table class="inventory-table">
            <tr>
                <th>ID</th>
                <th>PRODUCT_ID</th>
                <th>QUANTITY</th>
                <th>AMOUNT</th>
                <th>CLIENT_ID</th>
            </tr>
            <tr v-for="sale in sales" :key="sale.id">
                <td>{{ sale.id }}</td>
                <td>{{ sale.product_id }}</td>
                <td>{{ sale.quantity }}</td>
                <td>{{ sale.amount }}</td>
                <td>{{ sale.client_id }}</td>
            </tr>
        </table>
    </div>
    <div>
        <form @submit.prevent.stop="DeleteInventories">
            <label>Elija el producto a descontinuar</label>
            <select v-model="dataform.id">
                <option v-for="inventory in inventories" :key="inventory.id" :value="inventory.id">{{ inventory.name }}</option>
            </select>
            <label>Ingrese la contraseña de administrador</label>
            <input type="password" required v-model="dataform.password">
            <button>Submit</button>
        </form>
    </div>
</template>

<script>

import { getinventory } from '@/services/inventory.api';
import { initinventory } from '@/services/inventory.api';
import { deleteinventory } from '@/services/inventory.api';
import { showpurchases } from '@/services/tools.api';
import { showsales } from '@/services/tools.api';
import { showeerr } from '@/services/tools.api';
import { showmcp } from '@/services/tools.api';

export default {
    data() {
        return {
            dataform: {
                id : '',
                password : '',
            },
            inventories: [],
            purchases: [],
            sales: [],
        }
    },
    mounted() {
        this.fetchInventories();
        this.ShowPurchases();
        this.ShowSales();
    },
    methods: {
        async fetchInventories() {
            const { products } = await getinventory();
            console.log('products: ', products, typeof(products));
            this.inventories = products;
            console.log('inventories: ', this.inventories, typeof(this.inventories));
        },
        async ShowPurchases() {
            const { purchases } = await showpurchases();
            console.log('purchases: ', purchases, typeof(message));
            this.purchases = purchases;
            console.log('purchases: ', this.purchases, typeof(this.purchases));
        },
        async ShowSales() {
            const { sales } = await showsales();
            console.log('sales: ', sales, typeof(message));
            this.sales = sales;
            console.log('sales: ', this.sales, typeof(this.sales));
        },
        async InitInventories() {
            const { message } = await initinventory();
            console.log('message: ', message, typeof(message));
        },
        async DeleteInventories() {
            const { message } = await deleteinventory(this.dataform);
            console.log('message: ', message, typeof(message));
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
