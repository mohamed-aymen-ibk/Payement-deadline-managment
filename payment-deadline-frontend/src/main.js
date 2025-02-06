import PrimeVue from 'primevue/config';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import 'primevue/resources/themes/saga-blue/theme.css';  // Choose the theme you prefer
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import App from "@/App.vue";
import {createApp} from "vue";

const app = createApp(App);
app.use(PrimeVue);
app.component('DataTable', DataTable);
app.component('PrimeColumn', Column);
app.mount('#app');
