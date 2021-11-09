import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:newstudentflutter/common/mvp/base_adapter.dart';
import 'package:newstudentflutter/common/widget/base/widget_base_nav.dart';
import 'package:newstudentflutter/common/widget/base/widget_standard_template.dart';

import 'template_p.dart';
import 'template_page.dart';

/*
 * V
 */
class TemplateVImp extends NAdapterState<TemplateP, TemplateWidget>
    implements TemplateV, AppWidgetCallback {
  Map<String, dynamic> arguments;

  TemplateVImp(this.arguments);

  @override
  TemplateP createPresenter() {
    return TemplatePImp();
  }

  @override
  Widget buildPhone(BuildContext context) {
    return WidgetAppNorm(
      this,
      appBarColor: Colors.red,
    );
  }

  @override
  Widget buildAppBar() {
    return NavBarCustom(
      "Title",
      isCenterTitle: true,
      titleBgColor: Colors.blue,
    );
  }

  @override
  Widget buildBody() {
    return Container(
      color: Colors.black12,
      child: Center(
        child: Text("Hello!"),
      ),
    );
  }
}
