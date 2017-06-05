<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/streetview/publish/v1/resources.proto

namespace Google\Streetview\Publish\V1;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 * Identifier for a photo.
 * </pre>
 *
 * Protobuf type <code>google.streetview.publish.v1.PhotoId</code>
 */
class PhotoId extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * Required. A base64 encoded identifier.
     * </pre>
     *
     * <code>string id = 1;</code>
     */
    private $id = '';

    public function __construct() {
        \GPBMetadata\Google\Streetview\Publish\V1\Resources::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * Required. A base64 encoded identifier.
     * </pre>
     *
     * <code>string id = 1;</code>
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * <pre>
     * Required. A base64 encoded identifier.
     * </pre>
     *
     * <code>string id = 1;</code>
     */
    public function setId($var)
    {
        GPBUtil::checkString($var, True);
        $this->id = $var;
    }

}

