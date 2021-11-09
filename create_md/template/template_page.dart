import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:newstudentflutter/common/mvp/base_adapter.dart';

import 'template_v.dart';

/*
 * 入口层
 * todo 描述业务
 */
class TemplatePage extends StatelessWidget {
  Map<String, dynamic> params;

  TemplatePage(this.params);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: TemplateWidget(this.params),
    );
  }
}

class TemplateWidget extends NAdapterWidget {
  Map<String, dynamic> arguments;

  TemplateWidget(this.arguments);

  @override
  State<StatefulWidget> createState() {
    return new TemplateVImp(this.arguments);
  }
}
