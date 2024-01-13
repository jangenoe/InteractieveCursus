* DIODES INCORPORATED AND ITS AFFILIATED COMPANIES AND SUBSIDIARIES (COLLECTIVELY, "DIODES") 
* PROVIDE THESE SPICE MODELS AND DATA (COLLECTIVELY, THE "SM DATA") "AS IS" AND WITHOUT ANY 
* REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY 
* OR FITNESS FOR A PARTICULAR PURPOSE, ANY WARRANTY ARISING FROM COURSE OF DEALING OR COURSE OF 
* PERFORMANCE, OR ANY WARRANTY THAT ACCESS TO OR OPERATION OF THE SM DATA WILL BE UNINTERRUPTED, 
* OR THAT THE SM DATA OR ANY SIMULATION USING THE SM DATA WILL BE ERROR FREE. TO THE MAXIMUM 
* EXTENT PERMITTED BY LAW, IN NO EVENT WILL DIODES BE LIABLE FOR ANY DIRECT OR INDIRECT, 
* SPECIAL, INCIDENTAL, PUNITIVE OR CONSEQUENTIAL DAMAGES ARISING OUT OF OR IN CONNECTION WITH 
* THE PRODUCTION OR USE OF SM DATA, HOWEVER CAUSED AND UNDER WHATEVER CAUSE OF ACTION OR THEORY 
* OF LIABILITY BROUGHT (INCLUDING, WITHOUT LIMITATION, UNDER ANY CONTRACT, NEGLIGENCE OR OTHER 
* TORT THEORY OF LIABILITY), EVEN IF DIODES HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES, 
* AND DIODES' TOTAL LIABILITY (WHETHER IN CONTRACT, TORT OR OTHERWISE) WITH REGARD TO THE SM 
* DATA WILL NOT, IN THE AGGREGATE, EXCEED ANY SUMS PAID BY YOU TO DIODES FOR THE SM DATA.



*DIODES_INC_MJD42C_SPICE_MODEL
*DATE=13Mar2023
*VERSION=1.0
*ORIGIN=DT
*SIMULATOR=SIMETRIX
*
.MODEL MJD42C  PNP (IS=82.4f NF=1.00 BF=202 VAF=180
+ IKF=21.03 ISE=3.2p NE=2.00 BR=40.00 NR=1.00 NK=0.94 ISC=71p NC=1.8
+ VAR=28.0 IKR=12.0 RE=47.9m RB=52.77m RC=15.77m RCO=0.002
+ XTB=1.6 CJE=223p VJE=1.10 MJE=0.500 CJC=229p VJC=0.300
+ MJC=0.300 TF=950p TR=64.1n EG=1.12
+ TRE1=0.001 TRB1=0.003 TRC1=0.003 GAMMA=1n )
*
*$
*
******************************************************************************
*                	 (c)  2023 Diodes Inc
*
*   Diodes Incorporated and its affiliated companies and subsidiaries 
*   (collectively, "Diodes") provide these spice models and data 
*   (collectively, the "SM data") "as is" and without any representations
*   or warranties, express or implied, including any warranty of
*   merchantability or fitness for a particular purpose, any warranty 
*   arising from course of dealing or course of performance, or any 
*   warranty that access to or operation of the SM data will be
*   uninterrupted, or that the SM data or any simulation using the SM data
*   will be error free.
*
*   To the maximum extent permitted by law, in no event will Diodes be
*   liable for any indirect, special, incidental, punitive or consequential
*   damages arising out of or in connection with the production or use of
*   SM data, however caused and under whatever cause of action or theory of
*   liability brought (including, without limitation, under any contract,
*   negligence or other tort theory of liability), even if Diodes has been
*   advised of the possibility of such damages, and Diodes' total liability
*   (whether in contract, tort or otherwise) with regard to the SM data
*   will not, in the aggregate, exceed any sums paid by you to Diodes for
*   the SM data
*
*   Diodes Zetex Semiconductors Ltd, Zetex Technology Park, Chadderton,
*   Oldham, United Kingdom, OL9 9LL
******************************************************************************