# modelling-coursework

#### Step 1: Train word vector model

		1.1 Download the Wiki data from https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2j
		
		1.2 Run TrainModel_1_wod2vec_process.py with arguments:
		
				TrainModel_1_wod2vec_process.py zhwiki-latest-pages-articles.xml.bz2 wiki.zh.txt
		1.3 Use opencc to translate from traditional Chinese to simplified Chinese. On linux, install opencc using "sudo apt get opencc".
				opencc -i wiki.zh.txt -o wiki.zh.simp.txt -c t2s.json
		1.4 Run TrainModel_2_jieba_participle.py directly
		1.5 Run TrainModel_3_train_word2vec_model.py directly
		1.6 Run TrainModel_4_model_match.py directly
#### Step 2:


		2.1 Run 1_process.py
		2.2 Run 2_cutsentence.py 
		The txt file needs to be manually converted to UDF-8 format before executing the code, 
		otherwise it will report Chinese encoding error
		2.3 Run 3_stopword.py
		2.4 Run 4_getwordvecs.py
		2.5 Run 5_pca_svm.py

##### Reference:



		This code is improved and implemented based on https://www.jianshu.com/p/ec27062bd453 and https://www.jianshu.com/p/233da896226a
		The original posts are about sentiment analysis for hotel review. And my report is about depression detect on social media
