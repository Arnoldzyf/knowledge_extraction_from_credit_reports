// OCR结果应体现整体文档结构
//		  应解决表格跨页问题

{
	'header-0':{	//一级标题样式
		'header-name':'个人信用报告',
		'content':['本人版'],  //所有处于该标题和下一个相邻标题之间的内容, 默认为[]
		'section':{		// 包含子标题及其内容
			'header-0-0':{  // 二级标题样式，以此类推
				'header-name':'报告基本信息',
				'content':[table],  // table为二维数组; 
									// 若table第一行只有一个元素, 提取该元素为table名称, 作为子header
									// 一个header的content里最多有一个table (尽量)

			},
			'header-0-1':{
				'header-name':'其他证件信息',
				'content':[table],
			},
			...
		}
	},
	'header-1':{
		'header-name':'个人基本信息',  //删除标题编号，只留标题内容
		'content':[],
		'section':{
			'header-1-0':{
				'header-name':'身份信息',
				'content':[table],
			},
			'header-1-1':{
				'header-name':'配偶信息',
				'content':[table],
			},
			...	
		}
	},
	...
}