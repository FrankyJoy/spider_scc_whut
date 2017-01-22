from bs4 import BeautifulSoup

html_doc = """
<html xmlns="http://www.w3.org/1999/xhtml" >
<head id="Head1"><meta http-equiv="Content-Type" content="text/html; charset=gb2312" /><title>
	【交通运输】赛集航运咨询（上海）有限公司
</title><meta name="keywords" content="武汉理工大学就业信息网,武汉理工大学就业指导中心" /><meta name="description" content="武汉理工大学就业信息网,武汉理工大学就业指导中心" />
<script language="javascript" src="js/jquery-1.7.min.js"></script>
<link href="css/style.css" rel="stylesheet" type="text/css" /></head>
<body>
    <form name="form1" method="post" action="vjread.aspx?id=59092b77-e994-4914-a83e-a1deb5cd61ea&amp;vj" id="form1">
<div>
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKLTY2MDAzOTYyMmRkHe2doW2CQNGXUexd0P/cOE9VYhU=" />
</div>


<div class="top" style="padding-top:2px; height:150px;"><img src="images/scc_banner.jpg" width="1000" /></div>
<div class="dh">
<ul class="daoh">
			<li class="w80"><a href="index.aspx">首页</a></li>
			<li class="onm z10"><a href="#" class="ona">中心介绍</a><s></s>
			 <div class="ondh z10" style="display: none">
			 	<a href="zxjs/center.html">中心领导</a>
				<a href="zxjs/center_duty.html">机构负责人</a>
				<a href="zxjs/center_job.html">工作职责</a>
			  </div>
			</li>
			<li class="onm"><a href="#"class="ona">招聘信息</a><s></s>
			<div class="ondh" style="display: none">
					<a href="vjlist.aspx?type=zhaopinginfo&vj">招聘信息</a>
					<a href="vjlist.aspx?type=zph&vj">招聘会信息</a>
			 </div></li>
			<!--<li class="onm"><a href="#" class="ona">就业服务</a><s></s>
			<div class="ondh" style="display: none">
			 	<a href="vjlist.aspx?type=bszhinan&vj">办事指导</a>
				<a href="vjlist.aspx?type=fagui&vj">政策法规</a>
			 </div>
			</li>-->
			<li><a href="vjlist.aspx?type=bszhinan&vj">办事指南</a></li>
			<li><a href="vjlist.aspx?type=fagui&vj">政策法规</a></li>
			<li class="onm"><a href="http://166.111.4.130:8080/?d=whut.emtoem.com" class="ona" target="_blank">职业指导</a><s></s>
				<div class="ondh " style="display: none">
					<a href="http://scc.whut.edu.cn/App/GuestBook/Default.aspx" target="_blank">杨老师在线</a>
					<a href="#" onclick="javascript:openNoBarWindow('/Choose.html',530,230);">就业指导</a>
			 </div>
			</li>
			<li class="w120"><a href="service.aspx">用人单位服务</a></li>
<li><a href="http://whut.websjy.com/" target="_blank">创业指导</a></li>
  </ul>
</div>
<script type="text/javascript">
function removeElement(id)
{
document.getElementById(id).style.display="none";
}
</script>
<div id="Div-ts" style="margin:8px auto; background:#FBE4C0; padding:10px 0; text-align:center; position:relative; border:1px solid #F9771F; width:998px">
<a href="javascript:;" onClick="removeElement('Div-ts')" style="height:10px; width:10px; text-decoration:none; font-size:16px; position:absolute; top:5px; right:10px;">×</a>
<a href="http://scc.whut.edu.cn/vjread.aspx?id=18df4bec-4673-4d07-b528-3d0c7a63849e&vj" target="_blank" style="font-size:14px; color:#FF0509;"><b>关于第三方人才机构举办联合招聘会的严正声明</b></a></div>
   <div class="nrbox">
	<div class="nr-mini">武汉理工大学 >>  【交通运输】赛集航运咨询（上海）有限公司</div>
	<div class="nr-img"><img src="images/nrimg.jpg" /></div>
		<h2 class="nr-tit">【交通运输】赛集航运咨询（上海）有限公司</h2>
		<p class="nr-fb">访问数：225   发布人：就业指导中心   发布时间:2017-01-13  <strong><font color="red">2017-01-13  </font></strong></p>
		<div class="nr"> <!--内容正文开始-->
		    <DIV class=Section1><SPAN style="FONT-SIZE: 14pt; FONT-FAMILY: 'Times New Roman'; COLOR: #262626">
<DIV class=Section1>
<P style="TEXT-ALIGN: center; MARGIN: 0pt"><SPAN style="FONT-SIZE: 22pt; FONT-FAMILY: '宋体'; COLOR: #666666">赛集航运咨询（上海）有限公司</SPAN></P>
<P style="TEXT-ALIGN: center; MARGIN: 0pt"><SPAN style="FONT-SIZE: 22pt; FONT-FAMILY: 'Calibri'; COLOR: #262626"></SPAN>&nbsp;</P>
<P style="MARGIN: 0pt"><SPAN style="FONT-SIZE: 14pt; FONT-FAMILY: '宋体'; COLOR: #262626">【公司信息】</SPAN></P>
<P style="MARGIN: 0pt; TEXT-INDENT: 28pt"><SPAN style="FONT-SIZE: 14pt; FONT-FAMILY: '宋体'; COLOR: #262626">主要负责为国内外各大石化企业和贸易商提供液体散装货物，包括化学品、液化天然气及成品油的运输业务和商务法规、海运咨询服务。 另外还包括为国内外化工品和气体船船东提供国内港口的保护代理及总代理服务，以及化工品和气体船的船舶买卖和新造船业务，向外国船东或租家介绍中国各类港口的信息、政策。</SPAN></P>
<P style="MARGIN: 0pt; TEXT-INDENT: 28pt"><SPAN style="FONT-SIZE: 14pt; FONT-FAMILY: '宋体'; COLOR: #262626">公司里大部分的员工有海事院校相关背景，工作氛围积极向上。</SPAN></P>
<P style="TEXT-ALIGN: justify; ORPHANS: 0; WIDOWS: 0; MARGIN: 0pt"><SPAN style="FONT-SIZE: 14pt; FONT-FAMILY: '宋体'; COLOR: #262626">目前来看，即便航运市场整体低迷，但是我司主营的化工品</SPAN><SPAN style="FONT-SIZE: 14pt; FONT-FAMILY: 'Lucida Grande'; COLOR: #262626">/</SPAN><SPAN style="FONT-SIZE: 14pt; FONT-FAMILY: '宋体'; COLOR: #262626">气体市场仍</SPAN><SPAN style="FONT-SIZE: 14pt; FONT-FAMILY: '宋体'; COLOR: #262626">保有一定的活跃度，在所有同事的共同努力下，公司正在不断地发展壮大。</SPAN></P>

"""
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
title_node = soup.title.get_text()
print(title_node)
##title_node = soup.find_all('h2',class_='nr-tit').get_text()
##title_node.
##print(title_node)
