
# Pārdošanas datu analizators / Sales Data Analyzer / Анализатор продаж

## LV

Šī ir grafiska programma Python valodā, kas palīdz analizēt pārdošanas datus no Excel vai 
CSV failiem. Programma aprēķina galvenos pārdošanas rādītājus: kopējo ieņēmumu, pārdoto 
preču skaitu, vidējo čeku, kā arī nosaka labākās un sliktākās preces.

Programma izmanto `pandas` bibliotēku datu apstrādei, `matplotlib` grafiku veidošanai un `Tkinter` 
grafiskā interfeisa izveidei. Lietotājs var ērti izvēlēties failu caur dialoglodziņu, un visi 
analīzes rezultāti tiek parādīti logā ar ritjoslu. Papildus programma veido trīs veidu grafikus: 
stabiņu diagrammu pa precēm, sektoru diagrammu pa kategorijām un līniju diagrammu pārdošanas 
dinamikai.

Projektu plānoju pakāpeniski paplašināt. Nākotnē vēlos pievienot pārdošanas prognozēšanu 
(izmantojot mašīnmācīšanos), eksportu uz PDF, integrāciju ar e-komercijas platformu API 
(Etsy, eBay, Amazon) un atskaišu automātisku nosūtīšanu pa e-pastu.

## EN

This is a graphical Python program that helps analyze sales data from Excel or CSV files. 
The program calculates key sales metrics: total revenue, total quantity sold, average order 
value, as well as identifies the best and worst performing products.

The program uses the `pandas` library for data processing, `matplotlib` for creating charts, 
and `Tkinter` for building the graphical user interface. Users can easily select a file 
through a dialog box, and all analysis results are displayed in a scrollable window. 
Additionally, the program creates three types of charts: a bar chart by product, a pie 
chart by category, and a line chart for sales dynamics.

I plan to gradually expand the project. In the future, I want to add sales forecasting 
(using machine learning), PDF export, integration with e-commerce platform APIs (Etsy, 
eBay, Amazon), and automatic report sending via email.

## RU

Это графическая программа на Python, которая помогает анализировать данные о продажах из 
файлов Excel или CSV. Программа рассчитывает основные показатели продаж: общую выручку, 
количество проданных товаров, средний чек, а также определяет лучшие и худшие товары.

Программа использует библиотеку `pandas` для обработки данных, `matplotlib` для построения 
графиков и `Tkinter` для создания графического интерфейса. Пользователь может удобно выбрать 
файл через диалоговое окно, а все результаты анализа отображаются в окне с прокруткой. 
Дополнительно программа строит три типа графиков: столбчатую диаграмму по товарам, круговую 
диаграмму по категориям и линейную диаграмму динамики продаж.

Проект планирую постепенно расширять. В будущем хочу добавить прогнозирование продаж 
(с использованием машинного обучения), экспорт в PDF, интеграцию с API торговых площадок 
(Etsy, eBay, Amazon) и автоматическую отправку отчётов по электронной почте.