const byId = id => document.getElementById(id);

csvData = CSVParse();
CountrySelected();
Calculate();

function CountrySelected()
{
    const country = byId("countries").value;
    byId("coal%").value = (csvData[country]).Coal;
	byId("gas%").value = (csvData[country]).Gas;
	byId("oil%").value = (csvData[country]).Oil;
	byId("hydro%").value = (csvData[country]).Hydro;
	byId("renew%").value = (csvData[country]).Renewable;
	byId("nuclear%").value = (csvData[country]).Nuclear;	
	Calculate();
}

function Calculate()
{
	const e = byId("powerUnit");
	const power = byId("power").value / e.options[e.selectedIndex].value;
	
	const totalPercentage = Number(byId("coal%").value) + Number(byId("gas%").value) + Number(byId("oil%").value) + Number(byId("hydro%").value) + Number(byId("renew%").value) + Number(byId("nuclear%").value) + Number(byId("custom%").value);
	byId("total%").textContent = Math.round(totalPercentage*10)/10 + "%";
	
	const kgCO2result = ((byId("coal%").value * byId("coalCO").value + byId("gas%").value * byId("gasCO").value + byId("oil%").value * byId("oilCO").value +
				  byId("hydro%").value * byId("hydroCO").value + byId("renew%").value * byId("renewCO").value + byId("nuclear%").value * byId("nuclearCO").value + 
				  byId("custom%").value * byId("customCO").value) / 100000) * 24 * 365.2422 * power; //Yes, I am accounting for the leap year. Yes, I am a nerd.
	const treesRequired = kgCO2result / 15.7;

	byId("kgCO2result").textContent = ((Math.ceil(kgCO2result)).toLocaleString('en')).replace(/,/g," ");
	byId("treesRequired").textContent = ((Math.ceil(treesRequired)).toLocaleString('en')).replace(/,/g," ");
	byId("priceRequired").textContent = ((Math.round(treesRequired / 10)).toLocaleString('en')).replace(/,/g," ");
}

function CSVParse()
{
	//CSV->JSON from /Sources/data.csv
	const rawData = `{"Albania":{"Coal":0,"Gas":0,"Oil":0,"Hydro":100,"Renewable":0,"Nuclear":0},"Algeria":{"Coal":0,"Gas":97.8,"Oil":1.8,"Hydro":0.4,"Renewable":0,"Nuclear":0},"Angola":{"Coal":0,"Gas":0,"Oil":46.8,"Hydro":53.2,"Renewable":0,"Nuclear":0},"Argentina":{"Coal":2.9,"Gas":47.7,"Oil":13.8,"Hydro":29,"Renewable":2.5,"Nuclear":4.1},"Armenia":{"Coal":0,"Gas":42.4,"Oil":0,"Hydro":25.7,"Renewable":0.1,"Nuclear":31.8},"Australia":{"Coal":61.2,"Gas":21.9,"Oil":2,"Hydro":7.4,"Renewable":7.5,"Nuclear":0},"Austria":{"Coal":8,"Gas":8.8,"Oil":1,"Hydro":66.6,"Renewable":14.6,"Nuclear":0},"Azerbaijan":{"Coal":0,"Gas":93.9,"Oil":0.2,"Hydro":5.3,"Renewable":0.4,"Nuclear":0},"Bahrain":{"Coal":0,"Gas":100,"Oil":0,"Hydro":0,"Renewable":0,"Nuclear":0},"Bangladesh":{"Coal":2,"Gas":82,"Oil":14.7,"Hydro":1.1,"Renewable":0.3,"Nuclear":0},"Belarus":{"Coal":0.1,"Gas":98,"Oil":1.1,"Hydro":0.3,"Renewable":0.4,"Nuclear":0},"Belgium":{"Coal":6.2,"Gas":27,"Oil":0.3,"Hydro":0.4,"Renewable":16.6,"Nuclear":47.2},"Benin":{"Coal":0,"Gas":0,"Oil":99.5,"Hydro":0,"Renewable":0.5,"Nuclear":0},"Bolivia":{"Coal":0,"Gas":70,"Oil":2,"Hydro":25.7,"Renewable":2.3,"Nuclear":0},"Bosnia and Herzegovina":{"Coal":62.8,"Gas":0.2,"Oil":0.3,"Hydro":36.7,"Renewable":0,"Nuclear":0},"Botswana":{"Coal":95.8,"Gas":0,"Oil":4.2,"Hydro":0,"Renewable":0,"Nuclear":0},"Brazil":{"Coal":4.5,"Gas":13.7,"Oil":6,"Hydro":63.2,"Renewable":9.9,"Nuclear":2.6},"Brunei Darussalam":{"Coal":0,"Gas":99,"Oil":1,"Hydro":0,"Renewable":0,"Nuclear":0},"Bulgaria":{"Coal":45.4,"Gas":4.6,"Oil":0.4,"Hydro":9.8,"Renewable":5.9,"Nuclear":33.8},"Cambodia":{"Coal":28.2,"Gas":0,"Oil":10.7,"Hydro":60.5,"Renewable":0.6,"Nuclear":0},"Cameroon":{"Coal":0,"Gas":12.9,"Oil":12.8,"Hydro":73.2,"Renewable":1,"Nuclear":0},"Canada":{"Coal":9.9,"Gas":9.4,"Oil":1.2,"Hydro":58.3,"Renewable":4.5,"Nuclear":16.4},"Chile":{"Coal":35.3,"Gas":16.9,"Oil":6.2,"Hydro":31.3,"Renewable":9.8,"Nuclear":0},"China":{"Coal":72.6,"Gas":2,"Oil":0.2,"Hydro":18.6,"Renewable":4.1,"Nuclear":2.3},"Hong Kong SAR, China":{"Coal":76.2,"Gas":23,"Oil":0.6,"Hydro":0,"Renewable":0.2,"Nuclear":0},"Colombia":{"Coal":10.2,"Gas":15.3,"Oil":0.2,"Hydro":71.1,"Renewable":3.1,"Nuclear":0},"Congo, Dem. Rep.":{"Coal":0,"Gas":0.1,"Oil":0,"Hydro":99.9,"Renewable":0,"Nuclear":0},"Congo, Rep.":{"Coal":0,"Gas":45.3,"Oil":0,"Hydro":54.7,"Renewable":0,"Nuclear":0},"Costa Rica":{"Coal":0,"Gas":0,"Oil":10.2,"Hydro":65.7,"Renewable":24,"Nuclear":0},"Cote d'Ivoire":{"Coal":0,"Gas":69.9,"Oil":6.1,"Hydro":23.1,"Renewable":0.8,"Nuclear":0},"Croatia":{"Coal":17.6,"Gas":7.5,"Oil":1,"Hydro":67,"Renewable":6.9,"Nuclear":0},"Cuba":{"Coal":0,"Gas":14.4,"Oil":81.6,"Hydro":0.5,"Renewable":3.5,"Nuclear":0},"Curacao":{"Coal":0,"Gas":0,"Oil":96.4,"Hydro":0,"Renewable":3.6,"Nuclear":0},"Cyprus":{"Coal":0,"Gas":0,"Oil":92.7,"Hydro":0,"Renewable":7.3,"Nuclear":0},"Czech Republic":{"Coal":51.5,"Gas":1.9,"Oil":0,"Hydro":2.2,"Renewable":8.5,"Nuclear":35.7},"Denmark":{"Coal":34.4,"Gas":6.5,"Oil":1,"Hydro":0,"Renewable":55.8,"Nuclear":0},"Dominican Republic":{"Coal":13.3,"Gas":21.5,"Oil":51.9,"Hydro":8.5,"Renewable":4.7,"Nuclear":0},"Ecuador":{"Coal":0,"Gas":13.3,"Oil":37.5,"Hydro":47.1,"Renewable":2,"Nuclear":0},"Egypt, Arab Rep.":{"Coal":0,"Gas":78.7,"Oil":12.2,"Hydro":8.1,"Renewable":0.9,"Nuclear":0},"El Salvador":{"Coal":0,"Gas":0,"Oil":40.3,"Hydro":27.6,"Renewable":32.1,"Nuclear":0},"Eritrea":{"Coal":0,"Gas":0,"Oil":99.5,"Hydro":0,"Renewable":0.5,"Nuclear":0},"Estonia":{"Coal":87.4,"Gas":0.6,"Oil":0.3,"Hydro":0.2,"Renewable":10.9,"Nuclear":0},"Ethiopia":{"Coal":0,"Gas":0,"Oil":0.1,"Hydro":95.6,"Renewable":4.3,"Nuclear":0},"Finland":{"Coal":17.4,"Gas":8.1,"Oil":0.3,"Hydro":19.7,"Renewable":18.9,"Nuclear":34.6},"France":{"Coal":2.2,"Gas":2.3,"Oil":0.3,"Hydro":11.3,"Renewable":5.1,"Nuclear":78.4},"Gabon":{"Coal":0,"Gas":38.9,"Oil":27,"Hydro":33.6,"Renewable":0.5,"Nuclear":0},"Georgia":{"Coal":0,"Gas":19.6,"Oil":0,"Hydro":80.4,"Renewable":0,"Nuclear":0},"Germany":{"Coal":45.8,"Gas":10,"Oil":0.9,"Hydro":3.1,"Renewable":23,"Nuclear":15.6},"Ghana":{"Coal":0,"Gas":18.2,"Oil":17.1,"Hydro":64.7,"Renewable":0,"Nuclear":0},"Greece":{"Coal":51.1,"Gas":13.5,"Oil":11,"Hydro":8.9,"Renewable":15.3,"Nuclear":0},"Guatemala":{"Coal":17.3,"Gas":0,"Oil":14.1,"Hydro":45.2,"Renewable":23.4,"Nuclear":0},"Haiti":{"Coal":0,"Gas":0,"Oil":91.3,"Hydro":8.7,"Renewable":0,"Nuclear":0},"Honduras":{"Coal":0.5,"Gas":0,"Oil":55.7,"Hydro":32.4,"Renewable":11.5,"Nuclear":0},"Hungary":{"Coal":20.8,"Gas":14.4,"Oil":0.2,"Hydro":1,"Renewable":9.7,"Nuclear":53.3},"Iceland":{"Coal":0,"Gas":0,"Oil":0,"Hydro":71,"Renewable":28.9,"Nuclear":0},"India":{"Coal":75.1,"Gas":4.9,"Oil":1.8,"Hydro":10.2,"Renewable":5.2,"Nuclear":2.8},"Indonesia":{"Coal":52.6,"Gas":24.6,"Oil":11.3,"Hydro":6.6,"Renewable":4.8,"Nuclear":0},"Iran, Islamic Rep.":{"Coal":0.2,"Gas":71.3,"Oil":21.7,"Hydro":5,"Renewable":0.1,"Nuclear":1.6},"Iraq":{"Coal":0,"Gas":21.9,"Oil":73.7,"Hydro":4.3,"Renewable":0,"Nuclear":0},"Ireland":{"Coal":24.9,"Gas":49.6,"Oil":0.7,"Hydro":2.7,"Renewable":21.8,"Nuclear":0},"Israel":{"Coal":49.6,"Gas":48.4,"Oil":0.5,"Hydro":0,"Renewable":1.5,"Nuclear":0},"Italy":{"Coal":16.7,"Gas":33.7,"Oil":5.1,"Hydro":21.1,"Renewable":22.3,"Nuclear":0},"Jamaica":{"Coal":0,"Gas":0,"Oil":90.2,"Hydro":3.3,"Renewable":6.5,"Nuclear":0},"Japan":{"Coal":33.7,"Gas":40.6,"Oil":11.2,"Hydro":7.9,"Renewable":6.1,"Nuclear":0},"Jordan":{"Coal":0,"Gas":7.1,"Oil":92.5,"Hydro":0.3,"Renewable":0,"Nuclear":0},"Kazakhstan":{"Coal":71.9,"Gas":19.2,"Oil":1,"Hydro":7.9,"Renewable":0,"Nuclear":0},"Kenya":{"Coal":0,"Gas":0,"Oil":18.5,"Hydro":35.8,"Renewable":45.7,"Nuclear":0},"Korea, Dem. People’s Rep.":{"Coal":24.1,"Gas":0,"Oil":3.3,"Hydro":72.6,"Renewable":0,"Nuclear":0},"Korea, Rep.":{"Coal":42.4,"Gas":23.9,"Oil":3.2,"Hydro":0.5,"Renewable":1.1,"Nuclear":28.7},"Kosovo":{"Coal":96.9,"Gas":0,"Oil":0.3,"Hydro":2.8,"Renewable":0,"Nuclear":0},"Kuwait":{"Coal":0,"Gas":33.7,"Oil":66.3,"Hydro":0,"Renewable":0,"Nuclear":0},"Kyrgyz Republic":{"Coal":7.4,"Gas":0.8,"Oil":0.6,"Hydro":91.3,"Renewable":0,"Nuclear":0},"Latvia":{"Coal":0,"Gas":45.5,"Oil":0,"Hydro":38.8,"Renewable":15.8,"Nuclear":0},"Lebanon":{"Coal":0,"Gas":0,"Oil":98.9,"Hydro":1.1,"Renewable":0,"Nuclear":0},"Libya":{"Coal":0,"Gas":53.7,"Oil":46.3,"Hydro":0,"Renewable":0,"Nuclear":0},"Lithuania":{"Coal":0.1,"Gas":47.2,"Oil":4.3,"Hydro":10.8,"Renewable":30,"Nuclear":0},"Luxembourg":{"Coal":0,"Gas":76.2,"Oil":0,"Hydro":5.7,"Renewable":15.3,"Nuclear":0},"Macedonia, FYR":{"Coal":69.5,"Gas":3.6,"Oil":2.8,"Hydro":22.5,"Renewable":1.6,"Nuclear":0},"Malaysia":{"Coal":37.9,"Gas":50.1,"Oil":2.4,"Hydro":9.1,"Renewable":0.6,"Nuclear":0},"Malta":{"Coal":0,"Gas":0,"Oil":96.7,"Hydro":0,"Renewable":3.3,"Nuclear":0},"Mauritius":{"Coal":42.9,"Gas":0,"Oil":36.7,"Hydro":3.1,"Renewable":17.2,"Nuclear":0},"Mexico":{"Coal":11.2,"Gas":57,"Oil":10.9,"Hydro":12.9,"Renewable":4.6,"Nuclear":3.2},"Moldova":{"Coal":0,"Gas":93.5,"Oil":0.3,"Hydro":5.9,"Renewable":0.3,"Nuclear":0},"Mongolia":{"Coal":92.3,"Gas":0,"Oil":4.5,"Hydro":0,"Renewable":3.2,"Nuclear":0},"Montenegro":{"Coal":44.8,"Gas":0,"Oil":0,"Hydro":55.2,"Renewable":0,"Nuclear":0},"Morocco":{"Coal":55,"Gas":19.5,"Oil":13.1,"Hydro":5.7,"Renewable":6.7,"Nuclear":0},"Mozambique":{"Coal":0,"Gas":8.8,"Oil":0,"Hydro":91.2,"Renewable":0,"Nuclear":0},"Myanmar":{"Coal":2,"Gas":35.2,"Oil":0.5,"Hydro":62.4,"Renewable":0,"Nuclear":0},"Namibia":{"Coal":0,"Gas":0,"Oil":0.9,"Hydro":99.1,"Renewable":0,"Nuclear":0},"Nepal":{"Coal":0,"Gas":0,"Oil":0,"Hydro":99.8,"Renewable":0.2,"Nuclear":0},"Netherlands":{"Coal":31.3,"Gas":49.8,"Oil":1.8,"Hydro":0.1,"Renewable":11.2,"Nuclear":4},"New Zealand":{"Coal":4.5,"Gas":16.3,"Oil":0,"Hydro":55.9,"Renewable":23.2,"Nuclear":0},"Nicaragua":{"Coal":0,"Gas":0,"Oil":46.1,"Hydro":8.9,"Renewable":45,"Nuclear":0},"Niger":{"Coal":71.6,"Gas":0,"Oil":27.8,"Hydro":0,"Renewable":0.6,"Nuclear":0},"Nigeria":{"Coal":0,"Gas":82.4,"Oil":0,"Hydro":17.6,"Renewable":0,"Nuclear":0},"Norway":{"Coal":0.1,"Gas":1.8,"Oil":0,"Hydro":96,"Renewable":1.7,"Nuclear":0},"Oman":{"Coal":0,"Gas":97.4,"Oil":2.6,"Hydro":0,"Renewable":0,"Nuclear":0},"Pakistan":{"Coal":0.2,"Gas":25.1,"Oil":39.7,"Hydro":29.8,"Renewable":0.4,"Nuclear":4.8},"Panama":{"Coal":7.4,"Gas":0,"Oil":36.8,"Hydro":54.2,"Renewable":1.6,"Nuclear":0},"Paraguay":{"Coal":0,"Gas":0,"Oil":0,"Hydro":100,"Renewable":0,"Nuclear":0},"Peru":{"Coal":0.7,"Gas":45.9,"Oil":1.2,"Hydro":48.8,"Renewable":3.4,"Nuclear":0},"Philippines":{"Coal":42.8,"Gas":24.2,"Oil":7.4,"Hydro":11.8,"Renewable":13.8,"Nuclear":0},"Poland":{"Coal":83,"Gas":3.4,"Oil":1,"Hydro":1.4,"Renewable":11.1,"Nuclear":0},"Portugal":{"Coal":23,"Gas":13.2,"Oil":2.6,"Hydro":30,"Renewable":30.8,"Nuclear":0},"Qatar":{"Coal":0,"Gas":100,"Oil":0,"Hydro":0,"Renewable":0,"Nuclear":0},"Romania":{"Coal":27.3,"Gas":12.4,"Oil":0.7,"Hydro":28.8,"Renewable":12.8,"Nuclear":17.9},"Russian Federation":{"Coal":14.9,"Gas":50.2,"Oil":1,"Hydro":16.5,"Renewable":0.1,"Nuclear":17},"Saudi Arabia":{"Coal":0,"Gas":51.2,"Oil":48.8,"Hydro":0,"Renewable":0,"Nuclear":0},"Senegal":{"Coal":0,"Gas":4.2,"Oil":83.6,"Hydro":8.7,"Renewable":1.8,"Nuclear":0},"Serbia":{"Coal":66.3,"Gas":0.7,"Oil":0,"Hydro":32.9,"Renewable":0.1,"Nuclear":0},"Singapore":{"Coal":1.1,"Gas":95.3,"Oil":0.7,"Hydro":0,"Renewable":1.7,"Nuclear":0},"Slovak Republic":{"Coal":12.4,"Gas":6,"Oil":1.1,"Hydro":15.5,"Renewable":7.4,"Nuclear":57.1},"Slovenia":{"Coal":21.9,"Gas":2.2,"Oil":0.2,"Hydro":35.5,"Renewable":3,"Nuclear":37.1},"South Africa":{"Coal":93,"Gas":0,"Oil":0.1,"Hydro":0.4,"Renewable":1,"Nuclear":5.5},"South Sudan":{"Coal":0,"Gas":0,"Oil":99.6,"Hydro":0,"Renewable":0.4,"Nuclear":0},"Spain":{"Coal":16.5,"Gas":17.2,"Oil":5.1,"Hydro":14.2,"Renewable":25.9,"Nuclear":20.8},"Sri Lanka":{"Coal":25.7,"Gas":0,"Oil":35.1,"Hydro":36.5,"Renewable":2.7,"Nuclear":0},"Sudan":{"Coal":0,"Gas":0,"Oil":21.7,"Hydro":78.3,"Renewable":0,"Nuclear":0},"Suriname":{"Coal":0,"Gas":0,"Oil":37.7,"Hydro":62.3,"Renewable":0,"Nuclear":0},"Sweden":{"Coal":0.6,"Gas":0.3,"Oil":0.2,"Hydro":41.5,"Renewable":14.3,"Nuclear":42.3},"Switzerland":{"Coal":0,"Gas":0.7,"Oil":0.1,"Hydro":54.3,"Renewable":3.8,"Nuclear":39.3},"Syrian Arab Republic":{"Coal":0,"Gas":64.4,"Oil":21.8,"Hydro":13.8,"Renewable":0,"Nuclear":0},"Tajikistan":{"Coal":0,"Gas":2.9,"Oil":0,"Hydro":97.1,"Renewable":0,"Nuclear":0},"Tanzania":{"Coal":0,"Gas":42.2,"Oil":15.5,"Hydro":41.6,"Renewable":0.6,"Nuclear":0},"Thailand":{"Coal":21.6,"Gas":68.3,"Oil":1,"Hydro":3.2,"Renewable":5.9,"Nuclear":0},"Togo":{"Coal":0,"Gas":0,"Oil":12,"Hydro":84.5,"Renewable":3.5,"Nuclear":0},"Trinidad and Tobago":{"Coal":0,"Gas":99.8,"Oil":0.2,"Hydro":0,"Renewable":0,"Nuclear":0},"Tunisia":{"Coal":0,"Gas":94.2,"Oil":1.8,"Hydro":0.3,"Renewable":2.8,"Nuclear":0},"Turkey":{"Coal":30.3,"Gas":47.9,"Oil":0.9,"Hydro":16.1,"Renewable":4.8,"Nuclear":0},"Turkmenistan":{"Coal":0,"Gas":100,"Oil":0,"Hydro":0,"Renewable":0,"Nuclear":0},"Ukraine":{"Coal":38.7,"Gas":7,"Oil":0.1,"Hydro":4.7,"Renewable":0.9,"Nuclear":48.6},"United Arab":{"Coal":0,"Gas":98.4,"Oil":1.3,"Hydro":0,"Renewable":0.3,"Nuclear":0},"United Kingdom":{"Coal":30.4,"Gas":30,"Oil":0.5,"Hydro":1.8,"Renewable":17.7,"Nuclear":19},"United States":{"Coal":39.7,"Gas":26.9,"Oil":0.9,"Hydro":6.1,"Renewable":6.9,"Nuclear":19.2},"Uruguay":{"Coal":0,"Gas":0,"Oil":9.1,"Hydro":74.2,"Renewable":16.8,"Nuclear":0},"Uzbekistan":{"Coal":4.1,"Gas":74.2,"Oil":0.4,"Hydro":21.4,"Renewable":0,"Nuclear":0},"Venezuela, RB":{"Coal":0,"Gas":17.7,"Oil":14,"Hydro":68.3,"Renewable":0,"Nuclear":0},"Vietnam":{"Coal":24.5,"Gas":33.5,"Oil":0.3,"Hydro":41.5,"Renewable":0.1,"Nuclear":0},"Yemen, Rep.":{"Coal":0,"Gas":38.6,"Oil":61.4,"Hydro":0,"Renewable":0,"Nuclear":0},"Zambia":{"Coal":0,"Gas":0,"Oil":2.8,"Hydro":97.2,"Renewable":0,"Nuclear":0},"Zimbabwe":{"Coal":43.9,"Gas":0,"Oil":0.5,"Hydro":54.2,"Renewable":1.4,"Nuclear":0},"World":{"Coal":40.7,"Gas":21.6,"Oil":4.1,"Hydro":16.2,"Renewable":6,"Nuclear":10.6},"East Asia & Pacific":{"Coal":60.6,"Gas":13.5,"Oil":2.2,"Hydro":15,"Renewable":4.2,"Nuclear":3.8},"Europe & Central":{"Coal":24.1,"Gas":24.3,"Oil":1.3,"Hydro":16.6,"Renewable":10.5,"Nuclear":22.4},"Latin America & Caribbean":{"Coal":6.5,"Gas":26,"Oil":10.6,"Hydro":46.5,"Renewable":6.4,"Nuclear":1.9},"Middle East & North Afrika":{"Coal":3.4,"Gas":64.1,"Oil":28.8,"Hydro":2.6,"Renewable":0.4,"Nuclear":0.3},"North America":{"Coal":35.7,"Gas":24.6,"Oil":1,"Hydro":12.9,"Renewable":6.6,"Nuclear":18.9},"South Asia":{"Coal":65.7,"Gas":9.1,"Oil":5.2,"Hydro":11.6,"Renewable":4.6,"Nuclear":2.8},"Sub­Saharan Africa":{"Coal":51.4,"Gas":8.6,"Oil":4.3,"Hydro":21.2,"Renewable":1.7,"Nuclear":3}}`;
	return JSON.parse(rawData);
}