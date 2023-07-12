<template>
    <br><br>
    <h1>Tools Page</h1>
    <button class="button" @click="InitInventories">Init Inventory</button>
    <button class="button" @click="fetchInventories">Update Inventory</button>
    <button class="button" @click="ShowPurchases">Update Purchases</button>
    <button class="button" @click="ShowSales">Update Sales</button>
    <button class="button" @click="ShowEerr">Update EERR</button>
    <button class="button" @click="ShowMcp">Update MCP</button>
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
        <h1>EERR</h1>
        <tr v-for="deerr in eerr">
            <td>{{ deerr }}</td>
        </tr>
    </div>
    <div>
        <h1>MCP</h1>
        <p>MCP at the moment: {{ mcp }}</p>
    </div>

    </div>
    <div v-else>
        <h1>Loading jobs...</h1>
    </div>
    <br>
</template>

<script>

import { getinventory } from '@/services/inventory.api';
import { initinventory } from '@/services/inventory.api';
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
            eerr: [],
            mcp: "",
        }
    },
    mounted() {
        this.fetchInventories();
        this.ShowPurchases();
        this.ShowSales();
        this.ShowEerr();
        this.ShowMcp();
    },
    methods: {
        async fetchInventories() {
            const { data } = await getinventory();
            console.log('products: ', data, typeof(data));
            this.inventories =data;
            console.log('inventories: ', this.inventories, typeof(this.inventories));
        },
        async ShowPurchases() {
            const { data } = await showpurchases();
            console.log('purchases: ', data, typeof(data));
            this.purchases = data;
            console.log('purchases: ', this.purchases, typeof(this.purchases));
        },
        async ShowSales() {
            const { data } = await showsales();
            console.log('sales: ', data, typeof(data));
            this.sales = data;
            console.log('sales: ', this.sales, typeof(this.sales));
        },
        async InitInventories() {
            const { data } = await initinventory();
            console.log('message: ', data, typeof(data));
        },
        async ShowEerr() {
            const { data } = await showeerr();
            console.log('message: ', data, typeof(data));
            this.eerr = data;
            console.log('eerr: ', this.eerr, typeof(this.eerr));
        },
        async ShowMcp() {
            const { data } = await showmcp();
            console.log('message: ', data, typeof(data));
            this.mcp = data;
            console.log('mcp: ', this.mcp, typeof(this.mcp));
        },
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

.button {
  display: inline-block;
  padding: 10px 20px;
  border-radius: 4px;
  margin-right: 15px; 
  border: 1px solid #337ab7;
  background-color: #337ab7;
  color: #fff;
  font-size: 14px;
  font-weight: bold;
  text-decoration: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #23527c;
}

</style>
