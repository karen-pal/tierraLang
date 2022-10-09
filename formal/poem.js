// Generated automatically by nearley, version 2.20.1
// http://github.com/Hardmath123/nearley
(function () {
function id(x) { return x[0]; }

	// Moo lexer documention is here:
	// https://github.com/no-context/moo

	const moo = require("moo")
	const lexer = moo.compile({
	  ws:     /[ \t]+/,
	  prep: ["como", "sobre", "cubierto de", "en", "tu", "en tu", "el", "la", "en la", "en el", "del", "de", "de la", "las", "la", "de las", "se", "con una", "con", "por las"],
	  sust : ["el cielo", "mirada", "color", "calor", "misterio", "mañana", "flor", "viento", "alma", "piel de los vientos", "calle de tierra", "rocío de estrellas", "luna", "los junes", "voz", "la voz", "de una serenata", "serenata", "quietudes"],
	  verbo: ["brilla","abraza","sopla","tiene","rezando","despierta", "me abraza", "se enciende", "despierta", "cuelga", "saca", "se trepa"],
      sep: "#",
      NL:      { match: /\n/, lineBreaks: true },
	});
var grammar = {
    Lexer: lexer,
    ParserRules: [
    {"name": "MAIN", "symbols": ["VERSO", (lexer.has("sep") ? {type: "sep"} : sep), "VERSO", (lexer.has("sep") ? {type: "sep"} : sep), "VERSO"]},
    {"name": "VERSO", "symbols": ["PREPSUSTCOM"]},
    {"name": "VERSO", "symbols": ["PREPSUST"]},
    {"name": "VERSO", "symbols": ["VERBO"]},
    {"name": "PREPSUSTCOM", "symbols": ["PREPSUST", (lexer.has("ws") ? {type: "ws"} : ws), "PREPSUST"]},
    {"name": "PREPSUST", "symbols": [(lexer.has("prep") ? {type: "prep"} : prep), (lexer.has("ws") ? {type: "ws"} : ws), (lexer.has("sust") ? {type: "sust"} : sust)], "postprocess": 
        ([first,  , sec]) => {
                return {
                    type: "prepsust",
                    prep: first.value,
                    sust: sec.value,
                    lenPrep: first.value.length,
                    lenSust: sec.value.length,
                    len: first.value.length + sec.value.length
                    }
        }
                                },
    {"name": "VERBO", "symbols": [(lexer.has("verbo") ? {type: "verbo"} : verbo)], "postprocess": 
        ([first]) => {
                return {
                    verb:first.value,
                    type: first.type,
                    len:first.value.length
                    }
            }
        }
]
  , ParserStart: "MAIN"
}
if (typeof module !== 'undefined'&& typeof module.exports !== 'undefined') {
   module.exports = grammar;
} else {
   window.grammar = grammar;
}
})();
