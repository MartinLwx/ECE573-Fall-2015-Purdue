// Generated from /Users/martinlwx/Documents/forGit/ECE573-Fall-2015-Purdue/Projects/Project01.Scanner/toy/Micro.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MicroLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INTLITERAL=1, FLOATLITERAL=2, KEYWORDS=3, IDENTIFIER=4, QUOTE=5, STRINGLITERAL=6, 
		OPERATOR=7, COMMENT=8, WS=9;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"DIGIT", "LETTER", "INTLITERAL", "FLOATLITERAL", "KEYWORDS", "IDENTIFIER", 
			"QUOTE", "STRINGLITERAL", "OPERATOR", "COMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, "'\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INTLITERAL", "FLOATLITERAL", "KEYWORDS", "IDENTIFIER", "QUOTE", 
			"STRINGLITERAL", "OPERATOR", "COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MicroLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Micro.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13\u00ae\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\3\2\3\2\3\3\3\3\3\4\6\4\37\n\4\r\4\16\4 \3\5\7\5$\n\5"+
		"\f\5\16\5\'\13\5\3\5\3\5\6\5+\n\5\r\5\16\5,\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0082\n\6\3\7\3\7\7\7\u0086\n\7\f\7\16"+
		"\7\u0089\13\7\3\b\3\b\3\t\3\t\7\t\u008f\n\t\f\t\16\t\u0092\13\t\3\t\3"+
		"\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a0\n\n\3\13\3\13\3\13"+
		"\3\13\7\13\u00a6\n\13\f\13\16\13\u00a9\13\13\3\f\3\f\3\f\3\f\2\2\r\3\2"+
		"\5\2\7\3\t\4\13\5\r\6\17\7\21\b\23\t\25\n\27\13\3\2\n\3\2\62;\4\2C\\c"+
		"|\5\2\62;C\\c|\7\2GGQQSSVW``\6\2,-//\61\61??\6\2*+..=>@@\4\2\f\f\17\17"+
		"\5\2\13\f\17\17\"\"\2\u00c7\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3"+
		"\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2"+
		"\2\3\31\3\2\2\2\5\33\3\2\2\2\7\36\3\2\2\2\t%\3\2\2\2\13\u0081\3\2\2\2"+
		"\r\u0083\3\2\2\2\17\u008a\3\2\2\2\21\u008c\3\2\2\2\23\u009f\3\2\2\2\25"+
		"\u00a1\3\2\2\2\27\u00aa\3\2\2\2\31\32\t\2\2\2\32\4\3\2\2\2\33\34\t\3\2"+
		"\2\34\6\3\2\2\2\35\37\5\3\2\2\36\35\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !"+
		"\3\2\2\2!\b\3\2\2\2\"$\5\3\2\2#\"\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2"+
		"\2&(\3\2\2\2\'%\3\2\2\2(*\7\60\2\2)+\5\3\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2"+
		"\2\2,-\3\2\2\2-\n\3\2\2\2./\7R\2\2/\60\7T\2\2\60\61\7Q\2\2\61\62\7I\2"+
		"\2\62\63\7T\2\2\63\64\7C\2\2\64\u0082\7O\2\2\65\66\7D\2\2\66\67\7G\2\2"+
		"\678\7I\2\289\7K\2\29\u0082\7P\2\2:;\7G\2\2;<\7P\2\2<\u0082\7F\2\2=>\7"+
		"H\2\2>?\7W\2\2?@\7P\2\2@A\7E\2\2AB\7V\2\2BC\7K\2\2CD\7Q\2\2D\u0082\7P"+
		"\2\2EF\7T\2\2FG\7G\2\2GH\7C\2\2H\u0082\7F\2\2IJ\7Y\2\2JK\7T\2\2KL\7K\2"+
		"\2LM\7V\2\2M\u0082\7G\2\2NO\7K\2\2O\u0082\7H\2\2PQ\7G\2\2QR\7N\2\2RS\7"+
		"U\2\2S\u0082\7G\2\2TU\7H\2\2U\u0082\7K\2\2VW\7H\2\2WX\7Q\2\2X\u0082\7"+
		"T\2\2YZ\7T\2\2Z[\7Q\2\2[\u0082\7H\2\2\\]\7E\2\2]^\7Q\2\2^_\7P\2\2_`\7"+
		"V\2\2`a\7K\2\2ab\7P\2\2bc\7W\2\2c\u0082\7G\2\2de\7D\2\2ef\7T\2\2fg\7G"+
		"\2\2gh\7C\2\2h\u0082\7M\2\2ij\7T\2\2jk\7G\2\2kl\7V\2\2lm\7W\2\2mn\7T\2"+
		"\2n\u0082\7P\2\2op\7K\2\2pq\7P\2\2q\u0082\7V\2\2rs\7X\2\2st\7Q\2\2tu\7"+
		"K\2\2u\u0082\7F\2\2vw\7U\2\2wx\7V\2\2xy\7T\2\2yz\7K\2\2z{\7P\2\2{\u0082"+
		"\7I\2\2|}\7H\2\2}~\7N\2\2~\177\7Q\2\2\177\u0080\7C\2\2\u0080\u0082\7V"+
		"\2\2\u0081.\3\2\2\2\u0081\65\3\2\2\2\u0081:\3\2\2\2\u0081=\3\2\2\2\u0081"+
		"E\3\2\2\2\u0081I\3\2\2\2\u0081N\3\2\2\2\u0081P\3\2\2\2\u0081T\3\2\2\2"+
		"\u0081V\3\2\2\2\u0081Y\3\2\2\2\u0081\\\3\2\2\2\u0081d\3\2\2\2\u0081i\3"+
		"\2\2\2\u0081o\3\2\2\2\u0081r\3\2\2\2\u0081v\3\2\2\2\u0081|\3\2\2\2\u0082"+
		"\f\3\2\2\2\u0083\u0087\5\5\3\2\u0084\u0086\t\4\2\2\u0085\u0084\3\2\2\2"+
		"\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\16"+
		"\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008b\7$\2\2\u008b\20\3\2\2\2\u008c"+
		"\u0090\5\17\b\2\u008d\u008f\t\5\2\2\u008e\u008d\3\2\2\2\u008f\u0092\3"+
		"\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0093\3\2\2\2\u0092"+
		"\u0090\3\2\2\2\u0093\u0094\5\17\b\2\u0094\22\3\2\2\2\u0095\u0096\7<\2"+
		"\2\u0096\u00a0\7?\2\2\u0097\u00a0\t\6\2\2\u0098\u0099\7#\2\2\u0099\u00a0"+
		"\7?\2\2\u009a\u00a0\t\7\2\2\u009b\u009c\7>\2\2\u009c\u00a0\7?\2\2\u009d"+
		"\u009e\7@\2\2\u009e\u00a0\7?\2\2\u009f\u0095\3\2\2\2\u009f\u0097\3\2\2"+
		"\2\u009f\u0098\3\2\2\2\u009f\u009a\3\2\2\2\u009f\u009b\3\2\2\2\u009f\u009d"+
		"\3\2\2\2\u00a0\24\3\2\2\2\u00a1\u00a2\7/\2\2\u00a2\u00a3\7/\2\2\u00a3"+
		"\u00a7\3\2\2\2\u00a4\u00a6\n\b\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2"+
		"\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\26\3\2\2\2\u00a9\u00a7"+
		"\3\2\2\2\u00aa\u00ab\t\t\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\b\f\2\2\u00ad"+
		"\30\3\2\2\2\13\2 %,\u0081\u0087\u0090\u009f\u00a7\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}