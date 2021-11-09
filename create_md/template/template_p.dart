import 'package:newstudentflutter/common/mvp/base_adapter.dart';
import 'package:newstudentflutter/common/mvp/mvp.dart';

import 'template_m.dart';
import 'template_state.dart';

/*
 * 展示层
 */
abstract class TemplateV extends NV {}

/*
 * 数据层
 */
abstract class TemplateM extends NM {}

/*
 * 控制层
 */
abstract class TemplateP extends NP<TemplateV, TemplateM, TemplateModel> {}

/*
 * 逻辑实现
 */
class TemplatePImp extends TemplateP {
  @override
  IModel createModel() {
    return TemplateMImp();
  }
}
