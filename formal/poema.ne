@{%
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
%}

# Pass your lexer with @lexer:
@lexer lexer


MAIN -> VERSO %sep VERSO %sep VERSO
VERSO -> PREPSUSTCOM | PREPSUST | VERBO

PREPSUSTCOM -> PREPSUST %ws PREPSUST
PREPSUST
    -> %prep %ws %sust  {%
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
                        %}
VERBO
    -> %verbo {%
                ([first]) => {
                        return {
                            verb:first.value,
                            type: first.type,
                            len:first.value.length
                            }
                    }
                %}


