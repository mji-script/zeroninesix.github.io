
import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm";

const supabaseUrl = 'https://bvswdrtnvlikkdoxssle.supabase.co';
const supabaseKey = 'sb_publishable_SHVUrMe_SuNz-5ZgWz0q4g_CCRIASff';

const supabase = createClient(supabaseUrl, supabaseKey);

const button = document.getElementById('sendbutton');
const userinput = document.getElementById('userinput');

button.addEventListener('click', async () => {
    const testoInserito = userinput.value;

    if (testoInserito.length > 15) {
        alert('Il testo deve essere massimo di 15 caratteri.');
        return;
    }

    try {
        const { data, error } = await supabase
            .from('messaggi')
            .update({ testo: testoInserito })
            .eq('id', 1);

        if (error) throw error;
        console.log('Record aggiornato:', data);
    } 

    catch (err) {
        console.error('Errore Supabase:', err);
        alert('Errore Supabase: ' + err.message);
    }
});