# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:31:54 2019

@author: aqsha
"""

possibleq = ["Afghanistan",
"Albania",
"Algeria",
"Andorra",
"Angola",
"Antigua and Barbuda",
"Argentina",
"Armenia",
"Australia",
"Austria",
"Azerbaijan",
"Bahamas",
"Bahrain",
"Bangladesh",
"Barbados",
"Belarus",
"Belgium",
"Belize",
"Benin",
"Bhutan",
"Bolivia",
"Bosnia and Herzegovina",
"Botswana",
"Brazil",
"Brunei",
"Bulgaria",
"Burkina Faso",
"Burundi",
"Cambodia",
"Cameroon",
"Canada",
"Cape Verde",
"Central African Republic",
"Chad",
"Chile",
"China",
"Colombia",
"Comoros",
"Kongolese Republic",
"DR Congo",
"Costa Rica",
"Cote d’Ivoire",
"Croatia",
"Cuba",
"Cyprus",
"Czechia",
"Denmark",
"Djibouti",
"Dominica",
"Dominican Republic",
"East Timor (Timor-Leste)",
"Ecuador",
"Egypt",
"El Salvador",
"Equatorial Guinea",
"Eritrea",
"Estonia",
"Ethiopia",
"Micronesia",
"Fiji",
"Finland",
"France",
"French Guyana",
"Gabon",
"The Gambia",
"Georgia",
"Germany",
"Ghana",
"Greece",
"Grenada",
"Guatemala",
"Guinea",
"Guinea-Bissau",
"Guyana",
"Haiti",
"Honduras",
"Hungary",
"Iceland",
"India",
"Indonesia",
"Iran",
"Iraq",
"Ireland",
"Israel",
"Italy",
"Jamaica",
"Japan",
"Jordan",
"Kazakhstan",
"Kenya",
"Kiribati",
"North Korea",
"South Korea",
"Kosovo",
"Kuwait",
"Kyrgyzstan",
"Laos",
"Latvia",
"Lebanon",
"Lesotho",
"Liberia",
"Libya",
"Liechtenstein",
"Lithuania",
"Luxembourg",
"Macedonia",
"Madagascar",
"Malawi",
"Malaysia",
"Maldives",
"Mali",
"Malta",
"Marshall Islands",
"Mauritania",
"Mauritius",
"Mexico",
"Moldova",
"Monaco",
"Mongolia",
"Montenegro",
"Morocco",
"Mozambique",
"Myanmar (Burma)",
"Namibia",
"Nauru",
"Nepal",
"Netherlands",
"New Zealand",
"Nicaragua",
"Niger",
"Nigeria",
"Norway",
"Oman",
"Pakistan",
"Palau",
"Panama",
"Papua New Guinea",
"Paraguay",
"Peru",
"Philippines",
"Poland",
"Portugal",
"Qatar",
"Romania",
"Russia",
"Rwanda",
"Saint Kitts and Nevis",
"Saint Lucia",
"Saint Vincent and the Grenadines",
"Samoa",
"San Marino",
"Sao Tome and Principe",
"Saudi Arabia",
"Senegal",
"Serbia",
"Seychelles",
"Sierra Leone",
"Singapore",
"Slovakia",
"Slovenia",
"Solomon Islands",
"Somalia",
"South Africa",
"South Sudan",
"Spain",
"Sri Lanka",
"Sudan",
"Suriname",
"Swaziland",
"Sweden",
"Switzerland",
"Syria",
"Taiwan",
"Tajikistan",
"Tanzania",
"Thailand",
"Togo",
"Tonga",
"Trinidad and Tobago",
"Tunisia",
"Turkey",
"Turkmenistan",
"Tuvalu",
"Uganda",
"Ukraine",
"United Arab Emirates",
"United Kingdom",
"United States of America",
"Uruguay",
"Uzbekistan",
"Vanuatu",
"Vatican City (or Holy See)",
"Venezuela",
"Vietnam",
"Yemen",
"Zambia",
"Zimbabwe"]

possiblea = ["Kabul",
"Tirana",
"Algiers",
"Andorra la Vella",
"Luanda",
"Saint John's",
"Buenos Aires",
"Yerevan",
"Canberra",
"Vienna",
"Baku",
"Nassau",
"Manama",
"Dhaka",
"Bridgetown",
"Minsk",
"Brussels",
"Belmopan",
"Porto Novo",
"Thimphu",
"La Paz",
"Sarajevo",
"Gaborone",
"Brasilia",
"Bandar Seri Begawan",
"Sofia",
"Ouagadougou",
"Gitega",
"Phnom Penh",
"Yaounde",
"Ottawa",
"Praia",
"Bangui",
"N'Djamena",
"Santiago",
"Beijing",
"Bogota",
"Moroni",
"Kinshasa",
"Brazzaville",
"San Jose",
"Yamoussoukro",
"Zagreb",
"Havana",
"Nicosia",
"Prague",
"Copenhagen",
"Djibouti",
"Roseau",
"Santo Domingo",
"Dili",
"Quito",
"Cairo",
"San Salvador",
"Malabo",
"Asmara",
"Tallinn",
"Addis Ababa",
"Palikir",
"Suva",
"Helsinki",
"Paris",
"Cayenne",
"Libreville",
"Banjul",
"Tbilisi",
"Berlin",
"Accra",
"Athens",
"Saint George's",
"Guatemala City",
"Conakry",
"Bissau",
"Georgetown",
"Port au Prince",
"Tegucigalpa",
"Budapest",
"Reykjavik",
"New Delhi",
"Jakarta",
"Tehran",
"Baghdad",
"Dublin",
"Jerusalem",
"Rome",
"Kingston",
"Tokyo",
"Amman",
"Astana",
"Nairobi",
"Tarawa Atoll",
"Pyongyang",
"Seoul",
"Pristina",
"Kuwait City",
"Bishkek",
"Vientiane",
"Riga",
"Beirut",
"Maseru",
"Monrovia",
"Tripoli",
"Vaduz",
"Vilnius",
"Luxembourg",
"Skopje",
"Antananarivo",
"Lilongwe",
"Kuala Lumpur",
"Male",
"Bamako",
"Valletta",
"Majuro",
"Nouakchott",
"Port Louis",
"Mexico City",
"Chisinau",
"Monaco",
"Ulaanbaatar",
"Podgorica",
"Rabat",
"Maputo",
"Naypyidaw",
"Windhoek",
"No capital",
"Kathmandu",
"Amsterdam",
"Wellington",
"Managua",
"Niamey",
"Abuja",
"Oslo",
"Muscat",
"Islamabad",
"Melekeok",
"Panama City",
"Port Moresby",
"Asuncion",
"Lima",
"Manila",
"Warsaw",
"Lisbon",
"Doha",
"Bucharest",
"Moscow",
"Kigali",
"Basseterre",
"Castries",
"Kingstown",
"Apia",
"San Marino",
"Sao Tome",
"Riyadh",
"Dakar",
"Belgrade",
"Victoria",
"Freetown",
"Singapore",
"Bratislava",
"Ljubljana",
"Honiara",
"Mogadishu",
"Pretoria",
"Juba",
"Madrid",
"Colombo",
"Khartoum",
"Paramaribo",
"Mbabana",
"Stockholm",
"Bern",
"Damascus",
"Taipei",
"Dushanbe",
"Dodoma",
"Bangkok",
"Lome",
"Nuku'alofa",
"Port of Spain",
"Tunis",
"Ankara",
"Ashgabat",
"Funafuti",
"Kampala",
"Kiev",
"Abu Dhabi",
"London",
"Washington D.C",
"Montevideo",
"Tashkent",
"Port Vila",
"Vatican City",
"Caracas",
"Hanoi",
"Sanaa",
"Lusaka",
"Harare",
]
