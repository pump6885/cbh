
use "/Users/cbhbook/Desktop/codes_text/China Family Panle Studies/CFPS_the_Yangzte_River_Delta.dta", clear

binreg health i.wf1 i.edu i.c_age  sex chengxiang i.year i.prov_num, rr
// The actual sample size included in the model is used as the standard  sample =11658
// Generating quintiles based on the average annual disposable income of residents in the Yangtze River Delta  *****
xtile wf1 = fincome2_per, nq(5)


// Supplementary Table E5
centile fincome2_per if e(sample), centile(20,40,60,80)  
//Calculate the quintile boundaries for each income group in the sample finally included in the model, they are 9731, 17470, 26740, and 40520, namely.
tab wf1 if e(sample)
bysort wf1: summarize fincome2_per if e(sample), detail  //Median and quartiles for each quantile group

/*

1. health denotes residents' self-assessment of health   
2. wf1 denotes the wealth level of residents is divided into 5 subgroups  
3. c_age denotes five age groups 
4. edu denotes the education level of residents 
5. prov_num denotes the four provincial administrative units: Jiangsu Province, Zhejiang Province, Anhui Province and Shanghai
6. chengxiang denotes the location of residents, rural or urban area.
7. year denotes the specific survey year, 2014,2016 and 2018 namely.

*/ 

// Supplementary Table D1
***   1.  Description of the combined data from the three surveys from 2014 to 2018 *****
**** Chi-square test  ****
tabulate year health if e(sample)
tabulate wf1 health if e(sample), row chi2
nptrend health if e(sample), group(wf1) carmitage 
// carmitage refers to the Cochran-Armitage trend test, which is often used for trend analysis of binary results
nptrend health if e(sample), group(wf1) linear

tabulate c_age health if e(sample), row chi2
nptrend health if e(sample), group(c_age) carmitage 
nptrend health if e(sample), group(wf1) linear

tabulate edu health if e(sample), row chi2
nptrend health if e(sample), group(edu) carmitage 

tabulate sex health if e(sample), row chi2
tabulate chengxiang health if e(sample), row chi2
tab year health if e(sample), row chi2
tab prov_num health if e(sample), row chi2


***  There are overall differences in the chi-square test between the "year" and "prov_num"  *****
tabulate year health if e(sample), row chi2
nptrend health if e(sample), group(year) linear
tabulate prov_num health if e(sample), row chi2
nptrend health if e(sample), group(prov_num) carmitage


// Supplementary Table D2
****  2. final results  ****** 
*** 2014-2018 *****
putdocx begin
binreg health i.wf1 i.edu i.c_age  sex chengxiang i.year i.prov_num, rr
putdocx paragraph
putdocx text ("14-18")
putdocx text (e(cmdline))
putdocx table results = etable


// Supplementary Table D3
**** Sensitivity analysis *****
*** 2014 *****

binreg health i.wf1 i.edu i.c_age sex chengxiang i.prov_num if year ==1 , rr
putdocx paragraph
putdocx text ("14")
putdocx text (e(cmdline))
putdocx table results = etable
*** 2016 *****

binreg health i.wf1 i.edu i.c_age sex chengxiang i.prov_num if year ==2 , rr
putdocx paragraph
putdocx text ("16")
putdocx text (e(cmdline))
putdocx table results = etable

*** 2018 *****

binreg health i.wf1 i.edu i.c_age sex chengxiang i.prov_num if year ==3 , rr
putdocx paragraph
putdocx text ("18")
putdocx text (e(cmdline))
putdocx table results = etable

putdocx save "cfps_results_111.docx", replace
putdocx close










