# -*- coding: utf-8 -*-

# Author: Danilo Scorzoni Ré
# Date: 20/08/2014

# Loading necessary packages

import urllib2
import codecs
import unicodedata
import nltk
from BeautifulSoup import BeautifulSoup
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

# This function gets all the links in a URL, limited to a specified
# domain name.

def spider(url, closed_domain):

	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	url_list = []

	for tag in soup.findAll('a', href=True):
		full_url = tag['href'].replace('http://','').replace('https://','')
		domain = full_url.split('/')[0]
		if (domain == closed_domain):
			url_list.append(full_url)
		
	url_distinct = set(url_list)
	
	return url_distinct
	

# This function gets all the <p></p> contents of a URL

def getParagraphs(url):
	
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	
	paragraphs = []
	
	for paragraph in soup.findAll('p'):
		
		para_trat = acentos(nltk.clean_html(str(paragraph)))
		if (len(para_trat) > 50):
			paragraphs.append(para_trat.replace('\n',' ').replace('\t',' ').replace('\r',' ').replace('|',''))
	
	return paragraphs
	
def acentos(text):
	
	text = text.replace('&#33;','!')
	text = text.replace('&#34;','"')
	text = text.replace('&#35;','#')
	text = text.replace('&#36;','$')
	text = text.replace('&#37;','%')
	text = text.replace('&#38;','&')
	text = text.replace('&#39;','\'')
	text = text.replace('&#40;','(')
	text = text.replace('&#41;',')')
	text = text.replace('&#42;','*')
	text = text.replace('&#43;','+')
	text = text.replace('&#44;',',')
	text = text.replace('&#45;','-')
	text = text.replace('&#46;','.')
	text = text.replace('&#47;','/')
	text = text.replace('&#48;','0')
	text = text.replace('&#49;','1')
	text = text.replace('&#50;','2')
	text = text.replace('&#51;','3')
	text = text.replace('&#52;','4')
	text = text.replace('&#53;','5')
	text = text.replace('&#54;','6')
	text = text.replace('&#55;','7')
	text = text.replace('&#56;','8')
	text = text.replace('&#57;','9')
	text = text.replace('&#58;',':')
	text = text.replace('&#59;',';')
	text = text.replace('&#60;','<')
	text = text.replace('&#61;','=')
	text = text.replace('&#62;','>')
	text = text.replace('&#63;','?')
	text = text.replace('&#64;','@')
	text = text.replace('&#65;','A')
	text = text.replace('&#66;','B')
	text = text.replace('&#67;','C')
	text = text.replace('&#68;','D')
	text = text.replace('&#69;','E')
	text = text.replace('&#70;','F')
	text = text.replace('&#71;','G')
	text = text.replace('&#72;','H')
	text = text.replace('&#73;','I')
	text = text.replace('&#74;','J')
	text = text.replace('&#75;','K')
	text = text.replace('&#76;','L')
	text = text.replace('&#77;','M')
	text = text.replace('&#78;','N')
	text = text.replace('&#79;','O')
	text = text.replace('&#80;','P')
	text = text.replace('&#81;','Q')
	text = text.replace('&#82;','R')
	text = text.replace('&#83;','S')
	text = text.replace('&#84;','T')
	text = text.replace('&#85;','U')
	text = text.replace('&#86;','V')
	text = text.replace('&#87;','W')
	text = text.replace('&#88;','X')
	text = text.replace('&#89;','Y')
	text = text.replace('&#90;','Z')
	text = text.replace('&#91;','[')
	text = text.replace('&#92;','\\')
	text = text.replace('&#93;',']')
	text = text.replace('&#94;','^')
	text = text.replace('&#95;','_')
	text = text.replace('&#96;','`')
	text = text.replace('&#97;','a')
	text = text.replace('&#98;','b')
	text = text.replace('&#99;','c')
	text = text.replace('&#100;','d')
	text = text.replace('&#101;','e')
	text = text.replace('&#102;','f')
	text = text.replace('&#103;','g')
	text = text.replace('&#104;','h')
	text = text.replace('&#105;','i')
	text = text.replace('&#106;','j')
	text = text.replace('&#107;','k')
	text = text.replace('&#108;','l')
	text = text.replace('&#109;','m')
	text = text.replace('&#110;','n')
	text = text.replace('&#111;','o')
	text = text.replace('&#112;','p')
	text = text.replace('&#113;','q')
	text = text.replace('&#114;','r')
	text = text.replace('&#115;','s')
	text = text.replace('&#116;','t')
	text = text.replace('&#117;','u')
	text = text.replace('&#118;','v')
	text = text.replace('&#119;','w')
	text = text.replace('&#120;','x')
	text = text.replace('&#121;','y')
	text = text.replace('&#122;','z')
	text = text.replace('&#123;','{')
	text = text.replace('&#124;','|')
	text = text.replace('&#125;','}')
	text = text.replace('&#126;','~')
	text = text.replace('&#161;','')
	text = text.replace('&#162;','')
	text = text.replace('&#163;','')
	text = text.replace('&#164;','')
	text = text.replace('&#165;','')
	text = text.replace('&#166;','')
	text = text.replace('&#167;','')
	text = text.replace('&#168;','')
	text = text.replace('&#169;','')
	text = text.replace('&#170;','')
	text = text.replace('&#171;','')
	text = text.replace('&#172;','')
	text = text.replace('&#173;','')
	text = text.replace('&#174;','')
	text = text.replace('&#175;','')
	text = text.replace('&#176;','')
	text = text.replace('&#177;','')
	text = text.replace('&#178;','')
	text = text.replace('&#179;','')
	text = text.replace('&#180;','')
	text = text.replace('&#181;','')
	text = text.replace('&#182;','')
	text = text.replace('&#183;','')
	text = text.replace('&#184;','')
	text = text.replace('&#185;','')
	text = text.replace('&#186;','')
	text = text.replace('&#187;','')
	text = text.replace('&#188;','')
	text = text.replace('&#189;','')
	text = text.replace('&#190;','')
	text = text.replace('&#191;','')
	text = text.replace('&#192;','A')
	text = text.replace('&#193;','A')
	text = text.replace('&#194;','A')
	text = text.replace('&#195;','A')
	text = text.replace('&#196;','A')
	text = text.replace('&#197;','A')
	text = text.replace('&#198;','AE')
	text = text.replace('&#199;','C')
	text = text.replace('&#200;','E')
	text = text.replace('&#201;','E')
	text = text.replace('&#202;','E')
	text = text.replace('&#203;','E')
	text = text.replace('&#204;','I')
	text = text.replace('&#205;','I')
	text = text.replace('&#206;','I')
	text = text.replace('&#207;','I')
	text = text.replace('&#208;','D')
	text = text.replace('&#209;','N')
	text = text.replace('&#210;','O')
	text = text.replace('&#211;','O')
	text = text.replace('&#212;','O')
	text = text.replace('&#213;','O')
	text = text.replace('&#214;','O')
	text = text.replace('&#215;','')
	text = text.replace('&#216;','0')
	text = text.replace('&#217;','U')
	text = text.replace('&#218;','U')
	text = text.replace('&#219;','U')
	text = text.replace('&#220;','U')
	text = text.replace('&#221;','Y')
	text = text.replace('&#222;','')
	text = text.replace('&#223;','')
	text = text.replace('&#224;','a')
	text = text.replace('&#225;','a')
	text = text.replace('&#226;','a')
	text = text.replace('&#227;','a')
	text = text.replace('&#228;','a')
	text = text.replace('&#229;','a')
	text = text.replace('&#230;','ae')
	text = text.replace('&#231;','c')
	text = text.replace('&#232;','e')
	text = text.replace('&#233;','e')
	text = text.replace('&#234;','e')
	text = text.replace('&#235;','e')
	text = text.replace('&#236;','i')
	text = text.replace('&#237;','i')
	text = text.replace('&#238;','i')
	text = text.replace('&#239;','i')
	text = text.replace('&#240;','o')
	text = text.replace('&#241;','n')
	text = text.replace('&#242;','o')
	text = text.replace('&#243;','o')
	text = text.replace('&#244;','o')
	text = text.replace('&#245;','o')
	text = text.replace('&#246;','o')
	text = text.replace('&#247;','')
	text = text.replace('&#248;','')
	text = text.replace('&#249;','u')
	text = text.replace('&#250;','u')
	text = text.replace('&#251;','u')
	text = text.replace('&#252;','u')
	text = text.replace('&#253;','y')
	text = text.replace('&#254;','')
	text = text.replace('&#255;','y')
	text = text.replace('&#256;','A')
	text = text.replace('&Aacute;','A')
	text = text.replace('&aacute;','a')
	text = text.replace('&Acirc;','A')
	text = text.replace('&acirc;','a')
	text = text.replace('&Agrave;','A')
	text = text.replace('&agrave;','a')
	text = text.replace('&Aring;','A')
	text = text.replace('&aring;','a')
	text = text.replace('&Atilde;','A')
	text = text.replace('&atilde;','a')
	text = text.replace('&Auml;','A')
	text = text.replace('&auml;','a')
	text = text.replace('&AElig;','AE')
	text = text.replace('&aelig;','ae')
	text = text.replace('&Eacute;','E')
	text = text.replace('&eacute;','e')
	text = text.replace('&Ecirc;','E')
	text = text.replace('&ecirc;','e')
	text = text.replace('&Egrave;','E')
	text = text.replace('&egrave;','e')
	text = text.replace('&Euml;','E')
	text = text.replace('&euml;','e')
	text = text.replace('&ETH;','d')
	text = text.replace('&eth;','')
	text = text.replace('&Iacute;','I')
	text = text.replace('&iacute;','i')
	text = text.replace('&Icirc;','I')
	text = text.replace('&icirc;','i')
	text = text.replace('&Igrave;','I')
	text = text.replace('&igrave;','i')
	text = text.replace('&Iuml;','I')
	text = text.replace('&iuml;','i')
	text = text.replace('&Oacute;','O')
	text = text.replace('&oacute;','o')
	text = text.replace('&Ocirc;','O')
	text = text.replace('&ocirc;','o')
	text = text.replace('&Ograve;','O')
	text = text.replace('&ograve;','o')
	text = text.replace('&Oslash;','')
	text = text.replace('&oslash;','')
	text = text.replace('&Otilde;','O')
	text = text.replace('&otilde;','o')
	text = text.replace('&Ouml;','o')
	text = text.replace('&ouml;','o')
	text = text.replace('&Uacute;','U')
	text = text.replace('&uacute;','u')
	text = text.replace('&Ucirc;','U')
	text = text.replace('&ucirc;','u')
	text = text.replace('&Ugrave;','U')
	text = text.replace('&ugrave;','u')
	text = text.replace('&Uuml;','U')
	text = text.replace('&uuml;','u')
	text = text.replace('&Ccedil;','C')
	text = text.replace('&ccedil;','c')
	text = text.replace('&Ntilde;','N')
	text = text.replace('&ntilde;','n')
	text = text.replace('&Yacute;','Y')
	text = text.replace('&yacute;','y')
	text = text.replace('&quot;','"')
	text = text.replace('&lt;','')
	text = text.replace('&gt;','')
	text = text.replace('&amp;','')
	text = text.replace('&reg;','')
	text = text.replace('&copy;','')
	text = text.replace('&THORN;','')
	text = text.replace('&thorn;','')
	text = text.replace('&szlig;','')
	text = text.replace('1','')
	text = text.replace('2','')
	text = text.replace('3','')
	text = text.replace('4','')
	text = text.replace('5','')
	text = text.replace('6','')
	text = text.replace('7','')
	text = text.replace('8','')
	text = text.replace('9','')
	text = text.replace('0','')
	text = text.replace('"','')
	text = text.replace('!','')
	text = text.replace('@','')
	text = text.replace('#','')
	text = text.replace('$','')
	text = text.replace('%','')
	text = text.replace('&','')
	text = text.replace('*','')
	text = text.replace('(','')
	text = text.replace(')','')
	text = text.replace('-','')
	text = text.replace('_','')
	text = text.replace('+','')
	text = text.replace('=','')
	text = text.replace('.',' ')
	text = text.replace('|','')
	text = text.replace('\\','')
	text = text.replace('<','')
	text = text.replace('>','')
	text = text.replace(',','')
	text = text.replace(';','')
	text = text.replace(':','')
	text = text.replace('?','')
	text = text.replace('/','')
	text = text.replace('`','')
	text = text.replace('[','')
	text = text.replace('{','')
	text = text.replace('~','')
	text = text.replace('^','')
	text = text.replace(']','')
	text = text.replace(']','')
	
	return text

def outText(fname, text):
	
	fileOpen = codecs.open(fname, 'a', 'utf-8')
	fileOpen.write(text)
	fileOpen.close()

# Crawling Globo Esporte

links = spider('http://globoesporte.globo.com/','globoesporte.globo.com')

for link in links:
	
	ident = 'ESPORTE'
	try:
		prgs = getParagraphs('http://' + link)
	except:
		continue
	
	for p in prgs:
		print p
		outText('saida_ESPORTE_2.txt',ident + '|' + link + '|' + p + '\n')
	
	print '[CONCLUIDO] ' + link
	
