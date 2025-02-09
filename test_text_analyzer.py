import pytest
import re
from collections import Counter
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import langcodes
from textblob import TextBlob

from project import count_sentences
from project import count_words
from project import number_all_chars
from project import number_chars_no_spaces
from project import most_frequent_words
from project import get_language
from project import analyze_sentiment


def test_countsentences():
    assert count_sentences('oi .') == 1
    assert count_sentences("Hello. How are you?") == 2
    assert count_sentences('oi. oi. oi.') == 3
    assert count_sentences('Hi! how are you?') == 2
    assert count_sentences('Hi, how are you') == 1

def test_countwords():
    assert count_words('oi.') == 1
    assert count_words('oi olá oi.') == 3
    assert count_words('Once upon a time a language called python') == 8

def test_number_all_chars():
    assert number_all_chars('1234') == 4
    assert number_all_chars('olá') == 3
    assert number_all_chars('') == 0

def test_number_chars_no_spaces():
    assert number_chars_no_spaces('1 2 3') == 3
    assert number_chars_no_spaces('olá olé') == 6
    assert number_chars_no_spaces('Hello world, my name is Python') == 25

def test_most_frequent_words():
    text = "this is a test this is only a test"
    expected_output = [("this", 2), ("is", 2), ("a", 2), ("test", 2), ("only", 1)]
    result = most_frequent_words(text, 5)
    assert result == expected_output

def test_get_language():
    assert get_language('Bom dia') == 'Portuguese'
    assert get_language('Hallo! Wie geht es dir? Frohes Neues Jahr!') == 'German'
    assert get_language('Djien dobry! Jak się masz?') == 'Polish'
    assert get_language('Hello! How are you?') == 'English'
    assert get_language('A 25 de Abril de 1974, o Movimento das Forças Armadas, coroando a longa resistência do povo português e interpretando os seus sentimentos profundos, derrubou o regime fascista. Libertar Portugal da ditadura, da opressão e do colonialismo representou uma transformação revolucionária e o início de uma viragem histórica da sociedade portuguesa. A Revolução restituiu aos Portugueses os direitos e liberdades fundamentais. No exercício destes direitos e liberdades, os legítimos representantes do povo reúnem-se para elaborar uma Constituição que corresponde às aspirações do país. A Assembleia Constituinte afirma a decisão do povo português de defender a independência nacional, de garantir os direitos fundamentais dos cidadãos, de estabelecer os princípios basilares da democracia, de assegurar o primado do Estado de Direito democrático e de abrir caminho para uma sociedade socialista, no respeito da vontade do povo português, tendo em vista a construção de um país mais livre, mais justo e mais fraterno. A Assembleia Constituinte, reunida na sessão plenária de 2 de Abril de 1976, aprova e decreta a seguinte Constituição da República Portuguesa:') == 'Portuguese'
    assert get_language('Der Parlamentarische Rat hat am 23. Mai 1949 in Bonn am Rhein in öffentlicher Sitzung festgestellt, daß das am 8. Mai des Jahres 1949 vom Parlamentarischen Rat beschlossene Grundgesetz für die Bundesrepublik Deutschland in der Woche vom 16. bis 22. Mai 1949 durch die Volksvertretungen von mehr als Zweidritteln der beteiligten deutschen Länder angenommen worden ist. Auf Grund dieser Feststellung hat der Parlamentarische Rat, vertreten durch seine Präsidenten, das Grundgesetz ausgefertigt und verkündet.Das Grundgesetz wird hiermit gemäß Artikel 145 Abs. 3 im Bundesgesetzblatt veröffentlicht:') == 'German'
    assert get_language('W trosce o byt i przyszłość naszej Ojczyzny, odzyskawszy w 1989 roku możliwość suwerennego i demokratycznego stanowienia o Jej losie, my, Naród Polski - wszyscy obywatele Rzeczypospolitej, zarówno wierzący w Boga będącego źródłem prawdy, sprawiedliwości, dobra i piękna, jak i nie podzielający tej wiary,a te uniwersalne wartości wywodzący z innych źródeł,równi w prawach i w powinnościach wobec dobra wspólnego - Polski, wdzięczni naszym przodkom za ich pracę, za walkę o niepodległość okupioną ogromnymi ofiarami, za kulturę zakorzenioną w chrześcijańskim dziedzictwie Narodu i ogólnoludzkich wartościach, nawiązując do najlepszych tradycji Pierwszej i Drugiej Rzeczypospolitej, zobowiązani, by przekazać przyszłym pokoleniom wszystko, co cenne z ponad tysiącletniego dorobku, złączeni więzami wspólnoty z naszymi rodakami rozsianymi po świecie, świadomi potrzeby współpracy ze wszystkimi krajami dla dobra Rodziny Ludzkiej, pomni gorzkich doświadczeń z czasów, gdy podstawowe wolności i prawa człowieka były w naszej Ojczyźnie łamane, pragnąc na zawsze zagwarantować prawa obywatelskie, a działaniu instytucji publicznych zapewnić rzetelność i sprawność,w poczuciu odpowiedzialności przed Bogiem lub przed własnym sumieniem, ustanawiamy Konstytucję Rzeczypospolitej Polskiej jako prawa podstawowe dla państwa oparte na poszanowaniu wolności i sprawiedliwości, współdziałaniu władz, dialogu społecznym oraz na zasadzie pomocniczości umacniającej uprawnienia obywateli i ich wspólnot.') == 'Polish'


def test_analyze_sentiment():
    assert analyze_sentiment(".") == 0
    assert analyze_sentiment('super hyper mega happy') > 0
    assert analyze_sentiment('he was in trouble') < 0
