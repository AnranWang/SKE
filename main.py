#encoding=utf-8

# 解决cmd命令行下输出中文字符乱码问题(必须放置在文本最前面)
from __future__ import unicode_literals
import sys
import json
import os

# 操作中文必须语句，解决字符问题
reload(sys)
sys.setdefaultencoding('utf8')

import fileHandle
import textPreprocessing
import semanticsCount
import statisticsCount


def main(fileName, path):
    # 逻辑结构
    # 1、文本预处理(分词与词性标注、词语过滤、词语相关信息记录)
    print '------当前文本预处理操作------'
    wordsStatisticsData, wordsData = textPreprocessing.word_segmentation(fileName, path)
    # 2、词语语义贡献值计算(计算词语语义相似度、构建词语语义相思网络、计算词语居间度密度)
    print '------当前进行词语语义贡献值计算操作------'
    intermediaryDensity = semanticsCount.intermediaryDegreeDensity(fileName, path)
    # 3、计算词语统计特征值
    # keywordDatas = statisticsCount.tfidf()
    print '------当前进行词语统计特征值计算操作------'
    wordsStatisticsData = statisticsCount.wordsStatistics(wordsStatisticsData)
    print '------当前进行汇总计算操作------'
    # 4、计算词语关键度
    # 算法基础设定
    # 语义贡献值权重
    vdw = 0.6
    # 统计特征值权重
    tw = 0.4
    # 统计特征位置上权重
    locw1, locw2, locw3 = 0.5, 0.3, 0.3
    # 统计特征词长权重
    lenw = 0.01
    # 统计特征值中词性权重
    posw = 0.5
    # 统计特征中TF-IDF权重
    tfidfw = 0.8

    # 对收集到的词语进行重新遍历
    ske = {}
    for key in wordsStatisticsData.keys():
        # 取语义贡献值(假如居间度密度集合中不存在,补充为0)
        if intermediaryDensity.get(key):
            vdi = intermediaryDensity.get(key)
        else:
            vdi = 0

        # 暂时未加tfidf权值
        score = vdw * vdi + tw * (locw1 * float(wordsStatisticsData[key][0]) + lenw * int(len(key)) + posw * float(
                wordsStatisticsData[key][1]))
        ske[key] = score

    ske = sorted(ske.iteritems(), key=lambda d: d[1], reverse=True)  # 降序排列
    print json.dumps(ske, ensure_ascii=False)
    return ske

if __name__ == "__main__":
    pass
    # 进行关键词提取的文章
    curPath = fileHandle.get_cur_path()
    fileName = 'article2.txt'

    main(fileName, curPath)

    distanceData = [["命运", 0.6018461538461539], ["震惊", 0.5018461538461538], ["人民币", 0.40584615384615386], ["流动性", 0.40584615384615386], ["管理层", 0.40584615384615386], ["合理性", 0.40584615384615386], ["整体", 0.40184615384615385], ["方向", 0.40184615384615385], ["余额", 0.40184615384615385], ["时刻", 0.40184615384615385], ["基金", 0.40184615384615385], ["港股", 0.40184615384615385], ["股票", 0.40184615384615385], ["公司", 0.40184615384615385], ["资者", 0.40184615384615385], ["投身", 0.40184615384615385], ["主席", 0.40184615384615385], ["历史", 0.40184615384615385], ["收益", 0.40184615384615385], ["资格", 0.40184615384615385], ["缺席", 0.40184615384615385], ["资金", 0.40184615384615385], ["主观", 0.40184615384615385], ["数据", 0.40184615384615385], ["差异", 0.40184615384615385], ["部门", 0.40184615384615385], ["业务", 0.40184615384615385], ["官方", 0.40184615384615385], ["制度", 0.40184615384615385], ["总体", 0.40184615384615385], ["股市", 0.40184615384615385], ["政策", 0.40184615384615385], ["市值", 0.40184615384615385], ["股息", 0.40184615384615385], ["收盘", 0.40184615384615385], ["企业", 0.40184615384615385], ["措辞", 0.40184615384615385], ["快车道", 0.39661538461538465], ["交易日", 0.39661538461538465], ["大额", 0.39261538461538464], ["额度", 0.39261538461538464], ["笔者", 0.39261538461538464], ["节奏", 0.39261538461538464], ["两地", 0.39261538461538464], ["态度", 0.39261538461538464], ["总额", 0.39261538461538464], ["内地", 0.39261538461538464], ["全线", 0.39261538461538464], ["情况", 0.39261538461538464], ["途径", 0.39261538461538464], ["走势", 0.39261538461538464], ["作者", 0.39261538461538464], ["表态", 0.39261538461538464], ["人士", 0.39261538461538464], ["板块", 0.39261538461538464], ["月份", 0.39261538461538464], ["原因", 0.39261538461538464], ["太保", 0.38184615384615384], ["沪", 0.37784615384615383], ["中", 0.37323076923076925], ["投资", 0.3618461538461538], ["监管", 0.3618461538461538], ["财大气粗", 0.36061538461538456], ["发令枪", 0.35661538461538456], ["港", 0.35323076923076924], ["启动", 0.3526153846153846], ["预期", 0.3526153846153846], ["铺设", 0.3526153846153846], ["平淡", 0.34184615384615386], ["宽松", 0.34184615384615386], ["伟大", 0.34184615384615386], ["明显", 0.34184615384615386], ["重要", 0.34184615384615386], ["平稳", 0.34184615384615386], ["良久", 0.33261538461538465], ["谨慎", 0.33261538461538465], ["顺畅", 0.33261538461538465], ["掌握", 0.30492307692307696], ["表示", 0.3018461538461538], ["潜伏", 0.3018461538461538], ["结算", 0.3018461538461538], ["退出", 0.3018461538461538], ["买入", 0.3018461538461538], ["上限", 0.3018461538461538], ["出台", 0.3018461538461538], ["打算", 0.3018461538461538], ["精选", 0.3018461538461538], ["追究", 0.3018461538461538], ["限制", 0.3018461538461538], ["明确", 0.3018461538461538], ["切实", 0.3018461538461538], ["参与", 0.3018461538461538], ["卖出", 0.3018461538461538], ["获得", 0.3018461538461538], ["增加", 0.3018461538461538], ["放开", 0.3018461538461538], ["运行", 0.3018461538461538], ["优选", 0.3018461538461538], ["发表", 0.3018461538461538], ["正式", 0.3018461538461538], ["相关", 0.3018461538461538], ["收入", 0.3018461538461538], ["可喜", 0.3018461538461538], ["利于", 0.3018461538461538], ["开盘", 0.3018461538461538], ["行为", 0.3018461538461538], ["了解", 0.3018461538461538], ["意味着", 0.2966153846153846], ["相当于", 0.2966153846153846], ["称之为", 0.2966153846153846], ["引导", 0.2926153846153846], ["截至", 0.2926153846153846], ["严格", 0.2926153846153846], ["考虑", 0.2926153846153846], ["包括", 0.2926153846153846], ["青睐", 0.2926153846153846], ["兑现", 0.2926153846153846], ["备战", 0.2926153846153846], ["拟于", 0.2926153846153846], ["挖掘", 0.2926153846153846], ["贬值", 0.2926153846153846], ["披露", 0.2926153846153846], ["造成", 0.2926153846153846], ["关注", 0.2926153846153846], ["放行", 0.2926153846153846], ["发现", 0.2926153846153846], ["成交", 0.2926153846153846], ["具有", 0.2926153846153846], ["加大", 0.2926153846153846], ["出现", 0.2926153846153846], ["导致", 0.2926153846153846], ["引发", 0.2926153846153846], ["受益", 0.2926153846153846], ["开通", 0.2926153846153846], ["配置", 0.2926153846153846], ["升值", 0.2926153846153846], ["放松", 0.2926153846153846], ["允许", 0.2926153846153846], ["恰逢", 0.2926153846153846], ["走向", 0.2926153846153846], ["剩下", 0.2926153846153846], ["进入", 0.2926153846153846], ["渲染", 0.2926153846153846], ["成长", 0.2926153846153846], ["认为", 0.2926153846153846], ["观望", 0.2926153846153846], ["取得", 0.2926153846153846], ["是否", 0.2926153846153846], ["缩减", 0.2926153846153846], ["符合", 0.2926153846153846], ["不会", 0.2926153846153846], ["透露", 0.2926153846153846], ["通", 0.2670769230769231], ["优质", 0.20492307692307696], ["货币", 0.20492307692307696], ["金融", 0.20492307692307696], ["市场", 0.19261538461538466], ["形式", 0.19261538461538466], ["阶段", 0.19261538461538466], ["重点", 0.19261538461538466], ["特色", 0.17723076923076928], ["布局", 0.17723076923076928], ["资产", 0.17723076923076928], ["现实", 0.17723076923076928], ["交易", 0.17723076923076928], ["载入史册", 0.17600000000000002], ["个人观点", 0.17600000000000002], ["保险资金", 0.17600000000000002], ["积极探索", 0.17600000000000002], ["解决办法", 0.17600000000000002], ["主营业务", 0.17600000000000002], ["公共事业", 0.17600000000000002], ["直接原因", 0.17600000000000002], ["保险机构", 0.17600000000000002], ["知情", 0.1741538461538462], ["方面", 0.1741538461538462], ["有所", 0.1741538461538462], ["地产股", 0.17200000000000004], ["资举牌", 0.17200000000000004], ["证券网", 0.17200000000000004], ["概念股", 0.17200000000000004], ["科技股", 0.17200000000000004], ["绩优股", 0.17200000000000004], ["小盘股", 0.17200000000000004], ["风险", 0.17107692307692313], ["保监", 0.16800000000000004], ["险资", 0.16800000000000004], ["后险", 0.16800000000000004], ["小盘", 0.16800000000000004], ["博彩", 0.16800000000000004], ["资管", 0.16800000000000004], ["估值", 0.16800000000000004], ["对险", 0.16800000000000004], ["旗下", 0.16800000000000004], ["标的", 0.16800000000000004], ["体量", 0.16800000000000004], ["企", 0.16707692307692312], ["资", 0.16707692307692312], ["影响", 0.16492307692307692], ["约束", 0.16492307692307692], ["保监会", 0.15200000000000002], ["证监会", 0.15200000000000002], ["深交所", 0.15200000000000002], ["不利", 0.14492307692307693], ["巨大", 0.14492307692307693], ["严厉批评", 0.13599999999999998], ["期待已久", 0.13599999999999998], ["发生变化", 0.13599999999999998], ["寄予厚望", 0.13599999999999998], ["稳定", 0.13261538461538463], ["教育", 0.1310769230769231], ["探析", 0.128], ["高", 0.11323076923076925], ["险", 0.11323076923076925], ["利好", 0.10800000000000001], ["收购", 0.10492307692307692], ["直接", 0.10492307692307692], ["进行", 0.10492307692307692], ["存在", 0.10492307692307692], ["认可", 0.0926153846153846], ["显示", 0.0926153846153846], ["使用", 0.0926153846153846], ["发生", 0.07723076923076923], ["操作", 0.07415384615384614], ["探", 0.07323076923076924], ["无", 0.07323076923076924], ["尚待", 0.06799999999999999], ["重挫", 0.06799999999999999], ["获批", 0.06799999999999999], ["举牌", 0.06799999999999999], ["回撤", 0.06799999999999999], ["占比", 0.06799999999999999], ["加仓", 0.06799999999999999], ["通下", 0.06799999999999999], ["率", 0.06707692307692308], ["带", 0.06707692307692308], ["进", 0.06707692307692308], ["看", 0.06707692307692308], ["称", 0.06707692307692308]]

    routeData = [["命运", 0.7310769230769231], ["震惊", 0.6310769230769231], ["快车道", 0.535076923076923], ["人民币", 0.535076923076923], ["交易日", 0.535076923076923], ["流动性", 0.535076923076923], ["管理层", 0.535076923076923], ["合理性", 0.535076923076923], ["整体", 0.531076923076923], ["大额", 0.531076923076923], ["额度", 0.531076923076923], ["笔者", 0.531076923076923], ["节奏", 0.531076923076923], ["两地", 0.531076923076923], ["态度", 0.531076923076923], ["总额", 0.531076923076923], ["内地", 0.531076923076923], ["全线", 0.531076923076923], ["港股", 0.531076923076923], ["情况", 0.531076923076923], ["途径", 0.531076923076923], ["公司", 0.531076923076923], ["资者", 0.531076923076923], ["投身", 0.531076923076923], ["走势", 0.531076923076923], ["缺席", 0.531076923076923], ["作者", 0.531076923076923], ["表态", 0.531076923076923], ["数据", 0.531076923076923], ["人士", 0.531076923076923], ["差异", 0.531076923076923], ["部门", 0.531076923076923], ["板块", 0.531076923076923], ["总体", 0.531076923076923], ["股市", 0.531076923076923], ["市值", 0.531076923076923], ["股息", 0.531076923076923], ["措辞", 0.531076923076923], ["月份", 0.531076923076923], ["原因", 0.531076923076923], ["太保", 0.511076923076923], ["财大气粗", 0.499076923076923], ["发令枪", 0.49507692307692297], ["启动", 0.491076923076923], ["监管", 0.491076923076923], ["预期", 0.491076923076923], ["铺设", 0.491076923076923], ["平淡", 0.47107692307692306], ["宽松", 0.47107692307692306], ["良久", 0.47107692307692306], ["伟大", 0.47107692307692306], ["谨慎", 0.47107692307692306], ["平稳", 0.47107692307692306], ["顺畅", 0.47107692307692306], ["意味着", 0.43507692307692303], ["相当于", 0.43507692307692303], ["称之为", 0.43507692307692303], ["引导", 0.431076923076923], ["截至", 0.431076923076923], ["严格", 0.431076923076923], ["考虑", 0.431076923076923], ["包括", 0.431076923076923], ["青睐", 0.431076923076923], ["结算", 0.431076923076923], ["退出", 0.431076923076923], ["兑现", 0.431076923076923], ["备战", 0.431076923076923], ["拟于", 0.431076923076923], ["挖掘", 0.431076923076923], ["贬值", 0.431076923076923], ["上限", 0.431076923076923], ["披露", 0.431076923076923], ["造成", 0.431076923076923], ["关注", 0.431076923076923], ["放行", 0.431076923076923], ["发现", 0.431076923076923], ["成交", 0.431076923076923], ["出台", 0.431076923076923], ["打算", 0.431076923076923], ["具有", 0.431076923076923], ["精选", 0.431076923076923], ["追究", 0.431076923076923], ["加大", 0.431076923076923], ["明确", 0.431076923076923], ["切实", 0.431076923076923], ["出现", 0.431076923076923], ["卖出", 0.431076923076923], ["导致", 0.431076923076923], ["引发", 0.431076923076923], ["受益", 0.431076923076923], ["开通", 0.431076923076923], ["配置", 0.431076923076923], ["升值", 0.431076923076923], ["放开", 0.431076923076923], ["运行", 0.431076923076923], ["优选", 0.431076923076923], ["放松", 0.431076923076923], ["允许", 0.431076923076923], ["正式", 0.431076923076923], ["恰逢", 0.431076923076923], ["走向", 0.431076923076923], ["相关", 0.431076923076923], ["可喜", 0.431076923076923], ["剩下", 0.431076923076923], ["进入", 0.431076923076923], ["利于", 0.431076923076923], ["渲染", 0.431076923076923], ["成长", 0.431076923076923], ["认为", 0.431076923076923], ["开盘", 0.431076923076923], ["观望", 0.431076923076923], ["取得", 0.431076923076923], ["是否", 0.431076923076923], ["了解", 0.431076923076923], ["缩减", 0.431076923076923], ["符合", 0.431076923076923], ["不会", 0.431076923076923], ["透露", 0.431076923076923], ["中", 0.36707692307692313], ["港", 0.3563076923076923], ["掌握", 0.2895384615384616], ["方向", 0.28800000000000003], ["余额", 0.28800000000000003], ["时刻", 0.28800000000000003], ["优质", 0.28800000000000003], ["基金", 0.28800000000000003], ["货币", 0.28800000000000003], ["股票", 0.28800000000000003], ["主席", 0.28800000000000003], ["历史", 0.28800000000000003], ["收益", 0.28800000000000003], ["资格", 0.28800000000000003], ["资金", 0.28800000000000003], ["主观", 0.28800000000000003], ["业务", 0.28800000000000003], ["官方", 0.28800000000000003], ["制度", 0.28800000000000003], ["政策", 0.28800000000000003], ["收盘", 0.28800000000000003], ["企业", 0.28800000000000003], ["通", 0.2670769230769231], ["沪", 0.264], ["影响", 0.248], ["约束", 0.248], ["投资", 0.248], ["不利", 0.228], ["明显", 0.228], ["重要", 0.228], ["巨大", 0.228], ["金融", 0.18953846153846157], ["阶段", 0.18953846153846157], ["表示", 0.188], ["潜伏", 0.188], ["买入", 0.188], ["收购", 0.188], ["限制", 0.188], ["参与", 0.188], ["获得", 0.188], ["增加", 0.188], ["存在", 0.188], ["发表", 0.188], ["收入", 0.188], ["行为", 0.188], ["市场", 0.1864615384615385], ["形式", 0.1864615384615385], ["方面", 0.1864615384615385], ["重点", 0.1864615384615385], ["布局", 0.17723076923076928], ["资产", 0.17723076923076928], ["载入史册", 0.17600000000000002], ["个人观点", 0.17600000000000002], ["保险资金", 0.17600000000000002], ["积极探索", 0.17600000000000002], ["解决办法", 0.17600000000000002], ["主营业务", 0.17600000000000002], ["公共事业", 0.17600000000000002], ["直接原因", 0.17600000000000002], ["保险机构", 0.17600000000000002], ["特色", 0.1741538461538462], ["现实", 0.1741538461538462], ["知情", 0.1741538461538462], ["风险", 0.1741538461538462], ["有所", 0.1741538461538462], ["地产股", 0.17200000000000004], ["资举牌", 0.17200000000000004], ["证券网", 0.17200000000000004], ["概念股", 0.17200000000000004], ["科技股", 0.17200000000000004], ["绩优股", 0.17200000000000004], ["小盘股", 0.17200000000000004], ["交易", 0.17107692307692313], ["保监", 0.16800000000000004], ["险资", 0.16800000000000004], ["后险", 0.16800000000000004], ["小盘", 0.16800000000000004], ["博彩", 0.16800000000000004], ["资管", 0.16800000000000004], ["估值", 0.16800000000000004], ["对险", 0.16800000000000004], ["旗下", 0.16800000000000004], ["标的", 0.16800000000000004], ["体量", 0.16800000000000004], ["企", 0.16707692307692312], ["资", 0.16707692307692312], ["保监会", 0.15200000000000002], ["证监会", 0.15200000000000002], ["深交所", 0.15200000000000002], ["严厉批评", 0.13599999999999998], ["期待已久", 0.13599999999999998], ["发生变化", 0.13599999999999998], ["寄予厚望", 0.13599999999999998], ["教育", 0.1310769230769231], ["稳定", 0.12953846153846155], ["探析", 0.128], ["高", 0.11630769230769232], ["险", 0.11630769230769232], ["利好", 0.10800000000000001], ["认可", 0.08953846153846153], ["直接", 0.08953846153846153], ["进行", 0.08953846153846153], ["显示", 0.08646153846153845], ["使用", 0.08646153846153845], ["发生", 0.0803076923076923], ["操作", 0.07415384615384614], ["无", 0.07323076923076924], ["尚待", 0.06799999999999999], ["重挫", 0.06799999999999999], ["获批", 0.06799999999999999], ["举牌", 0.06799999999999999], ["回撤", 0.06799999999999999], ["占比", 0.06799999999999999], ["加仓", 0.06799999999999999], ["通下", 0.06799999999999999], ["率", 0.06707692307692308], ["探", 0.06707692307692308], ["带", 0.06707692307692308], ["进", 0.06707692307692308], ["看", 0.06707692307692308], ["称", 0.06707692307692308]]